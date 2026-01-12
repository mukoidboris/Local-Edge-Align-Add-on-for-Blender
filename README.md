# Blender Local Edge Align

This tool allows users to perform a "Scale to Zero" operation on selected edges, but instead of aligning all edges to a single shared center, **it aligns the two vertices of each individual edge to its own local center**.

This ensures that the edge remains centered while flattening it perfectly along the chosen axis (X, Y, or Z), correcting imperfections without collapsing the entire selection to a single point.

<img width="2126" height="724" alt="Tut" src="https://github.com/user-attachments/assets/abf81b4d-8b79-4ada-b60d-e231b8a6bb87" />
<img width="1671" height="730" alt="2" src="https://github.com/user-attachments/assets/f563fdd3-51c8-48ae-a64d-7e7625af567f" />

## ✨ Features

* **Local Alignment:** Flattens selected edges relative to their own local center.
* **Dedicated Axis Buttons:** Quick access buttons on the 3D Viewport's sidebar (N-Panel) for X, Y, and Z axis alignment.
* **Edit Mode Context:** The panel only appears when a Mesh object is selected and you are in Edit Mode.

## ⬇️ Installation

### 1. Download the Add-on

Download the `local_align_addon.py` file from the repository.

### 2. Install in Blender

1.  Open Blender and go to **Edit > Preferences**.
2.  Navigate to the **Add-ons** tab.
3.  Click the **Install...** button.
4.  Browse to the downloaded `local_align_addon.py` file and select it.
5.  Check the box next to **Mesh: Local Edge Align Tools** to enable the add-on.

## 🚀 Usage

1.  **Select a Mesh Object** and press **Tab** to enter **Edit Mode**.
2.  Press **N** in the 3D Viewport to open the sidebar panel.
3.  Click on the **Tools** tab.
4.  Locate the **Local Edge Align Tools** panel.
5.  **Select the edges** you wish to flatten.
6.  Click one of the dedicated buttons: **Align X**, **Align Y**, or **Align Z**.

The vertices of each selected edge will instantly be leveled along the chosen axis, preserving the overall position of the edge loop.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details (You should create a separate LICENSE file if you want to use the MIT License).

---
