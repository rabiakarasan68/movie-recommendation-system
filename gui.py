import tkinter as tk
from recommender import recommend 

def show_recommendations():
    movie_name = entry.get().strip() 

    if not movie_name:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a movie name.\n")
        result_text.config(state=tk.NORMAL)
        return  # Fonksiyonu burada durdur
    
    results = recommend(movie_name) 

    result_text.config(state=tk.NORMAL)

    result_text.delete(1.0, tk.END) 
    result_text.insert(tk.END, f"Recommendations for '{movie_name}':\n")
    for movie in results:
        result_text.insert(tk.END, movie + "\n") 
    result_text.config(state=tk.NORMAL)

window = tk.Tk() 
window.title("Movie Recommendation System")
window.geometry("400x400") 

label = tk.Label(window, text="Enter Movie Name:")
label.pack() 

entry = tk.Entry(window, width=40)
entry.pack()

button = tk.Button(window, text = "Recommend", command=show_recommendations)
button.pack()


result_text = tk.Text(window, height=10, width=40)
result_text.pack()

def disable_typing(event):
    if event.state & 0x4:
        return 
    return "break"

result_text.bind("<Key>", disable_typing)


result_text.bind("<Button-2>", lambda e: "break")  
result_text.bind("<Button-3>", lambda e: "break")  

window.mainloop()
