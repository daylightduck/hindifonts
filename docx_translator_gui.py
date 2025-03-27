# # Working gui do not mess with this shit

# import os
# import sys
# import tkinter as tk
# from tkinter import filedialog, ttk, messagebox
# from advanced_docx_translator import translate_docx_advanced

# class DocxTranslatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DOCX Translator")
#         self.root.geometry("600x400")
#         self.root.resizable(True, True)
        
#         # Create main frame
#         main_frame = ttk.Frame(root, padding="20")
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # File selection
#         file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
#         file_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(file_frame, text="Input DOCX File:").grid(row=0, column=0, sticky=tk.W, pady=5)
#         self.input_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.input_file_var, width=50).grid(row=0, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)
        
#         ttk.Label(file_frame, text="Output DOCX File:").grid(row=1, column=0, sticky=tk.W, pady=5)
#         self.output_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.output_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_output_file).grid(row=1, column=2, padx=5, pady=5)
        
#         # Translation options
#         options_frame = ttk.LabelFrame(main_frame, text="Translation Options", padding="10")
#         options_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(options_frame, text="Target Language:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
#         # Common language codes
#         self.languages = {
#             "Arabic": "ar",
#             "Chinese (Simplified)": "zh-CN",
#             "Chinese (Traditional)": "zh-TW",
#             "English": "en",
#             "French": "fr",
#             "German": "de",
#             "Hindi": "hi",
#             "Italian": "it",
#             "Japanese": "ja",
#             "Korean": "ko",
#             "Portuguese": "pt",
#             "Russian": "ru",
#             "Spanish": "es"
#         }
        
#         self.language_var = tk.StringVar(value="Spanish")
#         language_combo = ttk.Combobox(options_frame, textvariable=self.language_var, values=list(self.languages.keys()), width=20)
#         language_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Progress bar
#         progress_frame = ttk.Frame(main_frame)
#         progress_frame.pack(fill=tk.X, pady=10)
        
#         self.progress_var = tk.DoubleVar()
#         self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
#         self.progress_bar.pack(fill=tk.X, pady=5)
        
#         self.status_var = tk.StringVar(value="Ready")
#         status_label = ttk.Label(progress_frame, textvariable=self.status_var)
#         status_label.pack(anchor=tk.W, pady=5)
        
#         # Action buttons
#         button_frame = ttk.Frame(main_frame)
#         button_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Button(button_frame, text="Translate Document", command=self.translate_document, width=20).pack(side=tk.RIGHT, padx=5)
#         ttk.Button(button_frame, text="Exit", command=root.destroy, width=10).pack(side=tk.RIGHT, padx=5)
    
#     def browse_input_file(self):
#         file_path = filedialog.askopenfilename(
#             title="Select DOCX File",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.input_file_var.set(file_path)
#             # Auto-generate output file name
#             base_name = os.path.splitext(file_path)[0]
#             lang_code = self.languages.get(self.language_var.get(), "es")
#             self.output_file_var.set(f"{base_name}_{lang_code}.docx")
    
#     def browse_output_file(self):
#         file_path = filedialog.asksaveasfilename(
#             title="Save Translated DOCX As",
#             defaultextension=".docx",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.output_file_var.set(file_path)
    
#     def translate_document(self):
#         input_file = self.input_file_var.get()
#         output_file = self.output_file_var.get()
#         language = self.language_var.get()
#         lang_code = self.languages.get(language, "es")
        
#         if not input_file or not os.path.exists(input_file):
#             messagebox.showerror("Error", "Please select a valid input DOCX file.")
#             return
        
#         if not output_file:
#             messagebox.showerror("Error", "Please specify an output file path.")
#             return
        
#         # Update UI
#         self.status_var.set(f"Translating to {language}...")
#         self.progress_var.set(10)
#         self.root.update()
        
#         try:
#             # Call the translation function
#             translate_docx_advanced(input_file, output_file, lang_code)
            
#             # Update UI
#             self.progress_var.set(100)
#             self.status_var.set("Translation completed successfully!")
#             messagebox.showinfo("Success", f"Document has been translated to {language} and saved to:\n{output_file}")
        
#         except Exception as e:
#             self.status_var.set("Error during translation")
#             messagebox.showerror("Error", f"An error occurred during translation:\n{str(e)}")
        
#         finally:
#             self.progress_var.set(0)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DocxTranslatorApp(root)
#     root.mainloop()
    
# # I repeat do not mess with the above shit 

# import os
# import sys
# import tkinter as tk
# from tkinter import filedialog, ttk, messagebox
# from advanced_docx_translator import translate_docx_advanced, translation_using_groq


# class DocxTranslatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DOCX Translator")
#         self.root.geometry("600x450")
#         self.root.resizable(True, True)
        
#         # Create main frame
#         main_frame = ttk.Frame(root, padding="20")
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # File selection
#         file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
#         file_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(file_frame, text="Input DOCX File:").grid(row=0, column=0, sticky=tk.W, pady=5)
#         self.input_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.input_file_var, width=50).grid(row=0, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)
        
#         ttk.Label(file_frame, text="Output DOCX File:").grid(row=1, column=0, sticky=tk.W, pady=5)
#         self.output_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.output_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_output_file).grid(row=1, column=2, padx=5, pady=5)
        
#         # Translation options
#         options_frame = ttk.LabelFrame(main_frame, text="Translation Options", padding="10")
#         options_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(options_frame, text="Target Language:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
#         self.languages = {
#             "Arabic": "ar",
#             "Chinese (Simplified)": "zh-CN",
#             "Chinese (Traditional)": "zh-TW",
#             "English": "en",
#             "French": "fr",
#             "German": "de",
#             "Hindi": "hi",
#             "Italian": "it",
#             "Japanese": "ja",
#             "Korean": "ko",
#             "Portuguese": "pt",
#             "Russian": "ru",
#             "Spanish": "es"
#         }
        
#         self.language_var = tk.StringVar(value="Spanish")
#         language_combo = ttk.Combobox(options_frame, textvariable=self.language_var, values=list(self.languages.keys()), width=20)
#         language_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Translation Engine Selection
#         ttk.Label(options_frame, text="Translation Engine:").grid(row=1, column=0, sticky=tk.W, pady=5)
#         self.engine_var = tk.StringVar(value="Google Translate")
#         engine_combo = ttk.Combobox(options_frame, textvariable=self.engine_var, values=["Google Translate", "Groq Translation"], width=20)
#         engine_combo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Progress bar
#         progress_frame = ttk.Frame(main_frame)
#         progress_frame.pack(fill=tk.X, pady=10)
        
#         self.progress_var = tk.DoubleVar()
#         self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
#         self.progress_bar.pack(fill=tk.X, pady=5)
        
#         self.status_var = tk.StringVar(value="Ready")
#         status_label = ttk.Label(progress_frame, textvariable=self.status_var)
#         status_label.pack(anchor=tk.W, pady=5)
        
#         # Action buttons
#         button_frame = ttk.Frame(main_frame)
#         button_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Button(button_frame, text="Translate Document", command=self.translate_document, width=20).pack(side=tk.RIGHT, padx=5)
#         ttk.Button(button_frame, text="Exit", command=root.destroy, width=10).pack(side=tk.RIGHT, padx=5)
    
#     def browse_input_file(self):
#         file_path = filedialog.askopenfilename(
#             title="Select DOCX File",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.input_file_var.set(file_path)
#             base_name = os.path.splitext(file_path)[0]
#             lang_code = self.languages.get(self.language_var.get(), "es")
#             self.output_file_var.set(f"{base_name}_{lang_code}.docx")
    
#     def browse_output_file(self):
#         file_path = filedialog.asksaveasfilename(
#             title="Save Translated DOCX As",
#             defaultextension=".docx",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.output_file_var.set(file_path)
    
#     def translate_document(self):
#         input_file = self.input_file_var.get()
#         output_file = self.output_file_var.get()
#         language = self.language_var.get()
#         lang_code = self.languages.get(language, "es")
#         engine = self.engine_var.get()
        
#         if not input_file or not os.path.exists(input_file):
#             messagebox.showerror("Error", "Please select a valid input DOCX file.")
#             return
        
#         if not output_file:
#             messagebox.showerror("Error", "Please specify an output file path.")
#             return
        
#         self.status_var.set(f"Translating to {language} using {engine}...")
#         self.progress_var.set(10)
#         self.root.update()
        
#         try:
#             if engine == "Google Translate":
#                 translate_docx_advanced(input_file, output_file, lang_code)
           
            
#             self.progress_var.set(100)
#             self.status_var.set("Translation completed successfully!")
#             messagebox.showinfo("Success", f"Document has been translated to {language} using {engine} and saved to:\n{output_file}")
        
#         except Exception as e:
#             self.status_var.set("Error during translation")
#             messagebox.showerror("Error", f"An error occurred during translation:\n{str(e)}")
        
#         finally:
#             self.progress_var.set(0)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DocxTranslatorApp(root)
#     root.mainloop()


# working translation gui with groq 

# import os
# import tkinter as tk
# from tkinter import filedialog, ttk, messagebox
# from advanced_docx_translator import translate_docx_advanced

# class DocxTranslatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DOCX Translator")
#         self.root.geometry("600x450")
#         self.root.resizable(True, True)
        
#         # Create main frame
#         main_frame = ttk.Frame(root, padding="20")
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # File selection
#         file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
#         file_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(file_frame, text="Input DOCX File:").grid(row=0, column=0, sticky=tk.W, pady=5)
#         self.input_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.input_file_var, width=50).grid(row=0, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)
        
#         ttk.Label(file_frame, text="Output DOCX File:").grid(row=1, column=0, sticky=tk.W, pady=5)
#         self.output_file_var = tk.StringVar()
#         ttk.Entry(file_frame, textvariable=self.output_file_var, width=50).grid(row=1, column=1, padx=5, pady=5)
#         ttk.Button(file_frame, text="Browse...", command=self.browse_output_file).grid(row=1, column=2, padx=5, pady=5)
        
#         # Translation options
#         options_frame = ttk.LabelFrame(main_frame, text="Translation Options", padding="10")
#         options_frame.pack(fill=tk.X, pady=10)
        
#         ttk.Label(options_frame, text="Target Language:").grid(row=0, column=0, sticky=tk.W, pady=5)
#         self.languages = {
#             "Arabic": "ar",
#             "Chinese (Simplified)": "zh-CN",
#             "Chinese (Traditional)": "zh-TW",
#             "English": "en",
#             "French": "fr",
#             "German": "de",
#             "Hindi": "hi",
#             "Italian": "it",
#             "Japanese": "ja",
#             "Korean": "ko",
#             "Portuguese": "pt",
#             "Russian": "ru",
#             "Spanish": "es"
#         }
#         self.language_var = tk.StringVar(value="Spanish")
#         language_combo = ttk.Combobox(options_frame, textvariable=self.language_var, values=list(self.languages.keys()), width=20)
#         language_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Translation Engine Selection
#         ttk.Label(options_frame, text="Translation Engine:").grid(row=1, column=0, sticky=tk.W, pady=5)
#         self.engine_var = tk.StringVar(value="Google Translate")
#         engine_combo = ttk.Combobox(options_frame, textvariable=self.engine_var, values=["Google Translate", "Groq Translation"], width=20)
#         engine_combo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Progress bar
#         progress_frame = ttk.Frame(main_frame)
#         progress_frame.pack(fill=tk.X, pady=10)
#         self.progress_var = tk.DoubleVar()
#         self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
#         self.progress_bar.pack(fill=tk.X, pady=5)
#         self.status_var = tk.StringVar(value="Ready")
#         status_label = ttk.Label(progress_frame, textvariable=self.status_var)
#         status_label.pack(anchor=tk.W, pady=5)
        
#         # Action buttons
#         button_frame = ttk.Frame(main_frame)
#         button_frame.pack(fill=tk.X, pady=10)
#         ttk.Button(button_frame, text="Translate Document", command=self.translate_document, width=20).pack(side=tk.RIGHT, padx=5)
#         ttk.Button(button_frame, text="Exit", command=root.destroy, width=10).pack(side=tk.RIGHT, padx=5)
    
#     def browse_input_file(self):
#         file_path = filedialog.askopenfilename(
#             title="Select DOCX File",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.input_file_var.set(file_path)
#             base_name = os.path.splitext(file_path)[0]
#             lang_code = self.languages.get(self.language_var.get(), "es")
#             self.output_file_var.set(f"{base_name}_{lang_code}.docx")
    
#     def browse_output_file(self):
#         file_path = filedialog.asksaveasfilename(
#             title="Save Translated DOCX As",
#             defaultextension=".docx",
#             filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
#         )
#         if file_path:
#             self.output_file_var.set(file_path)
    
#     def translate_document(self):
#         input_file = self.input_file_var.get()
#         output_file = self.output_file_var.get()
#         language = self.language_var.get()
#         lang_code = self.languages.get(language, "es")
#         engine = self.engine_var.get()
        
#         if not input_file or not os.path.exists(input_file):
#             messagebox.showerror("Error", "Please select a valid input DOCX file.")
#             return
        
#         if not output_file:
#             messagebox.showerror("Error", "Please specify an output file path.")
#             return
        
#         self.status_var.set(f"Translating to {language} using {engine}...")
#         self.progress_var.set(10)
#         self.root.update()
        
#         try:
#             # Set engine code: 'groq' for Groq Translation, otherwise use 'google'
#             engine_code = 'groq' if engine == "Groq Translation" else 'google'
#             translate_docx_advanced(input_file, output_file, lang_code, engine=engine_code)
            
#             self.progress_var.set(100)
#             self.status_var.set("Translation completed successfully!")
#             messagebox.showinfo("Success", f"Document has been translated to {language} using {engine} and saved to:\n{output_file}")
        
#         except Exception as e:
#             self.status_var.set("Error during translation")
#             messagebox.showerror("Error", f"An error occurred during translation:\n{str(e)}")
        
#         finally:
#             self.progress_var.set(0)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DocxTranslatorApp(root)
#     root.mainloop()

import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox, scrolledtext
import threading
import queue
from advanced_docx_translator import translate_docx_advanced
import logging

# Create a custom handler that will put log messages in a queue
class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)

class DocxTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DOCX Translator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set up logging queue
        self.log_queue = queue.Queue()
        self.queue_handler = QueueHandler(self.log_queue)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.queue_handler.setFormatter(formatter)
        
        # Add the queue handler to the root logger
        root_logger = logging.getLogger()
        root_logger.addHandler(self.queue_handler)
        
        # Create main frame with two columns
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel for controls
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        
        # Right panel for logs
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # File selection
        file_frame = ttk.LabelFrame(left_panel, text="File Selection", padding="10")
        file_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(file_frame, text="Input DOCX File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_file_var = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.input_file_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(file_frame, text="Output DOCX File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.output_file_var = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.output_file_var, width=40).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_output_file).grid(row=1, column=2, padx=5, pady=5)
        
        # Translation options
        options_frame = ttk.LabelFrame(left_panel, text="Translation Options", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(options_frame, text="Target Language:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.languages = {
            "Arabic": "ar",
            "Chinese (Simplified)": "zh-CN",
            "Chinese (Traditional)": "zh-TW",
            "English": "en",
            "French": "fr",
            "German": "de",
            "Hindi": "hi",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Portuguese": "pt",
            "Russian": "ru",
            "Spanish": "es"
        }
        self.language_var = tk.StringVar(value="Spanish")
        language_combo = ttk.Combobox(options_frame, textvariable=self.language_var, values=list(self.languages.keys()), width=20)
        language_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Translation Engine Selection
        ttk.Label(options_frame, text="Translation Engine:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.engine_var = tk.StringVar(value="Google Translate")
        engine_combo = ttk.Combobox(options_frame, textvariable=self.engine_var, values=["Google Translate", "Groq Translation"], width=20)
        engine_combo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Batch size option
        ttk.Label(options_frame, text="Batch Size:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.batch_size_var = tk.IntVar(value=10)
        batch_spinner = ttk.Spinbox(options_frame, from_=1, to=50, textvariable=self.batch_size_var, width=5)
        batch_spinner.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(options_frame, text="(paragraphs per API call)").grid(row=2, column=2, sticky=tk.W, pady=5)
        
        # Progress and status
        progress_frame = ttk.LabelFrame(left_panel, text="Progress", padding="10")
        progress_frame.pack(fill=tk.X, pady=10)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, pady=5)
        
        stats_frame = ttk.Frame(progress_frame)
        stats_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(stats_frame, text="Status:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(stats_frame, textvariable=self.status_var).grid(row=0, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(stats_frame, text="API Calls:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.api_calls_var = tk.StringVar(value="0")
        ttk.Label(stats_frame, textvariable=self.api_calls_var).grid(row=1, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(stats_frame, text="Cached:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.cached_var = tk.StringVar(value="0")
        ttk.Label(stats_frame, textvariable=self.cached_var).grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Action buttons
        button_frame = ttk.Frame(left_panel)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Translate Document", command=self.start_translation_thread, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear Cache", command=self.clear_cache, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=root.destroy, width=10).pack(side=tk.RIGHT, padx=5)
        
        # Log display
        log_frame = ttk.LabelFrame(right_panel, text="Translation Log", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_display = scrolledtext.ScrolledText(log_frame, width=60, height=20)
        self.log_display.pack(fill=tk.BOTH, expand=True)
        self.log_display.config(state=tk.DISABLED)
        
        # Start the logging update timer
        self.update_log_display()
    
    def update_log_display(self):
        """Update the log display with new log messages"""
        # Check every 100ms for new log records
        while not self.log_queue.empty():
            record = self.log_queue.get()
            msg = self.queue_handler.format(record)
            self.log_display.config(state=tk.NORMAL)
            self.log_display.insert(tk.END, msg + '\n')
            self.log_display.see(tk.END)  # Scroll to the end
            self.log_display.config(state=tk.DISABLED)
            
            # Update status based on log messages
            if "API calls" in msg:
                try:
                    calls = int(msg.split("API calls")[0].strip().split()[-1])
                    self.api_calls_var.set(str(calls))
                except:
                    pass
            elif "cached translation" in msg.lower():
                try:
                    current = int(self.cached_var.get())
                    self.cached_var.set(str(current + 1))
                except:
                    pass
            
            # Update progress based on paragraph translation
            if "Translating document paragraph" in msg:
                try:
                    current, total = msg.split("paragraph")[1].strip().split("/")
                    current = int(current)
                    total = int(total)
                    percent = (current / total) * 100
                    self.progress_var.set(percent)
                except:
                    pass
        
        self.root.after(100, self.update_log_display)
    
    def browse_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Select DOCX File",
            filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
        )
        if file_path:
            self.input_file_var.set(file_path)
            base_name = os.path.splitext(file_path)[0]
            lang_code = self.languages.get(self.language_var.get(), "es")
            self.output_file_var.set(f"{base_name}_{lang_code}.docx")
    
    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Save Translated DOCX As",
            defaultextension=".docx",
            filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
        )
        if file_path:
            self.output_file_var.set(file_path)
    
    def clear_cache(self):
        """Clear the translation cache"""
        from advanced_docx_translator import translation_cache
        count = len(translation_cache)
        translation_cache.clear()
        messagebox.showinfo("Cache Cleared", f"Cleared {count} cached translations.")
        self.api_calls_var.set("0")
        self.cached_var.set("0")
    
    def start_translation_thread(self):
        # Reset counters
        self.progress_var.set(0)
        self.api_calls_var.set("0")
        self.cached_var.set("0")
        
        # Clear the log display
        self.log_display.config(state=tk.NORMAL)
        self.log_display.delete(1.0, tk.END)
        self.log_display.config(state=tk.DISABLED)
        
        # Start the translation process in a separate thread to keep the GUI responsive
        threading.Thread(target=self.translate_document, daemon=True).start()
    
    def translate_document(self):
        input_file = self.input_file_var.get()
        output_file = self.output_file_var.get()
        language = self.language_var.get()
        lang_code = self.languages.get(language, "es")
        engine = self.engine_var.get()
        
        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("Error", "Please select a valid input DOCX file.")
            return
        
        if not output_file:
            messagebox.showerror("Error", "Please specify an output file path.")
            return
        
        self.status_var.set(f"Translating to {language} using {engine}...")
        self.progress_var.set(5)  # Show initial progress
        self.root.update()
        
        try:
            # Set engine code: 'groq' for Groq Translation, otherwise use 'google'
            engine_code = 'groq' if engine == "Groq Translation" else 'google'
            
            # Logging will be handled by the queue handler
            logging.info(f"Starting translation of {input_file} to {lang_code} using {engine_code} engine")
            
            # Call the translation function
            translate_docx_advanced(input_file, output_file, lang_code, engine=engine_code)
            
            self.progress_var.set(100)
            self.status_var.set("Translation completed successfully!")
            messagebox.showinfo("Success", f"Document has been translated to {language} using {engine} and saved to:\n{output_file}")
        
        except Exception as e:
            self.status_var.set("Error during translation")
            logging.error(f"Translation error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred during translation:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DocxTranslatorApp(root)
    root.mainloop()
