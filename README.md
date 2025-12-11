# Efficient Page Replacement Algorithm Simulator
A simulator to compare three classic page replacement algorithms used in Operating Systems: **FIFO**, **LRU**, and **Optimal**. This project provides a GUI-based interface to input frame size and reference strings, visualize algorithm behavior, and compare page faults.
## 🚀 Project Overview
This simulator demonstrates how different page replacement algorithms behave when memory frames are limited. Users can enter the number of frames, input a reference string, run all three algorithms, view hit/miss patterns and page faults, and identify which algorithm performs best. The purpose is to help understand memory management and algorithm efficiency in Operating Systems.
## 📁 Project Structure
- `page_replacement.py` — Implements FIFO, LRU, and Optimal page replacement algorithms  
- `gui.py` — Tkinter-based graphical interface  
- `screenshots/` — Flowchart and GUI output screenshots  
- `final_os_report.pdf` — Full OS project report  
- `testcases.md` — Test cases with expected outputs  
- `.gitignore` — Ignores temporary/cache files  
## 🖥️ How to Run
### Requirements
Python 3.x and Tkinter (bundled with Python).
### Steps
1. Clone the repository:  
   git clone https://github.com/Mandeep2807/Efficient-Page-Replacement-Simulator 
2. Open the folder in your system.  
3. Run the GUI:  
   python gui.py  
4. Enter the number of frames and reference string (space-separated).  
5. Click **Run Simulation** to view FIFO, LRU, and Optimal results.
## 🧪 Sample Test Case
Frames: 3  
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3  
Expected Page Faults → FIFO: 9, LRU: 8, Optimal: 7  
All output screenshots are available in the `screenshots/` folder.
## 📸 Screenshots
Included screenshots:  
- Flowchart  
- GUI Input Interface  
- FIFO Output  
- LRU Output  
- Optimal Output  
Find them in the `screenshots/` directory.
## 🔧 Technologies Used
- Python  
- Tkinter GUI  
- ScrolledText widget for output  
- FIFO, LRU, Optimal algorithms  
## 🌱 Future Improvements
- Add error handling for invalid inputs  
- Add graphical charts for comparison  
- Export results to file  
- Add advanced algorithms (LFU, MFU, Second Chance)  
## 🌀 GitHub Revision Workflow
This project follows OS Lab requirements:  
- Minimum 7 commits  
- Feature branches used  
- Pull request + merge workflow  
- Clear commit messages showing project development  
Revision summary is included in the report.
## 📄 License
This project is created for academic and learning purposes related to Operating Systems.
