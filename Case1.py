from tkinter import *
from tkinter import colorchooser
from tkinter import ttk 

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Shape Drawing')
        self.root.geometry('800x600')

        self.create_widgets()

    def create_widgets(self):
        self.control_frame = Frame(self.root)
        self.control_frame.pack(side=LEFT, fill=Y)

        self.canvas = Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.pack(side=RIGHT)

        self.shape_object = StringVar(value='Line')
        ttk.Label(self.control_frame, text='Select Shape').pack(pady=5)
        self.shape_list = ttk.Combobox(self.control_frame, textvariable=self.shape_object, values=['line', 'rectangle', 'circle'])
        self.shape_list.pack(pady=5)

        self.coords_frame = Frame(self.control_frame)
        self.coords_frame.pack(pady=10)
        ttk.Label(self.coords_frame, text='Coordinates:').grid(row=0, column=0, columnspan=2)
        self.coord_labels = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
        self.coord_vars = {label: StringVar() for label in self.coord_labels}
        for i, label in enumerate(self.coord_labels):
            ttk.Label(self.coords_frame, text=label).grid(row=i//2+1, column=(i%2)*2)
            ttk.Entry(self.coords_frame, textvariable=self.coord_vars[label]).grid(row=i//2+1, column=(i%2)*2+1)

        self.thickness = StringVar(value='1')
        self.color_outline = StringVar(value='black')
        self.color_fill = StringVar(value='')

        ttk.Label(self.control_frame, text='Thickness:').pack(pady=5)
        ttk.Entry(self.control_frame, textvariable=self.thickness).pack(pady=5)

        ttk.Label(self.control_frame, text='Outline Color:').pack(pady=5)
        self.outline_color_button = Button(self.control_frame, text='Select Color', command=self.select_outline_color)
        self.outline_color_button.pack(pady=5)

        ttk.Label(self.control_frame, text='Fill Color:').pack(pady=5)
        self.fill_color_button = Button(self.control_frame, text='Select Color', command=self.select_fill_color)
        self.fill_color_button.pack(pady=5)

        self.draw_button = Button(self.control_frame, text='Draw', command=self.draw_object)
        self.draw_button.pack(pady=20)

    def select_outline_color(self):
        color_code = colorchooser.askcolor(title='Choose Outline Color')
        self.color_outline.set(color_code[1])

    def select_fill_color(self):
        color_code = colorchooser.askcolor(title='Choose Fill Color')
        self.color_fill.set(color_code[1])

    def draw_object(self):
        object_type = self.shape_object.get().lower()
        thickness = int(self.thickness.get())
        outline = self.color_outline.get()
        fill = self.color_fill.get()

        try:
            coords = [int(self.coord_vars[label].get()) for label in self.coord_labels if self.coord_vars[label].get()]
        except ValueError:
            print("Please Enter Valid Coordinates")
            return 

        if object_type == 'line':
            self.canvas.create_line(*coords, width=thickness, fill=outline)
        elif object_type == 'rectangle':
            self.canvas.create_polygon(coords, outline=outline, fill=fill, width=thickness)
        elif object_type == 'circle':
            if len(coords) < 3:
                print("Please enter valid coordinates for the circle.")
                return
            x, y, r = coords[0], coords[1], coords[2]
            self.canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline, fill=fill, width=thickness)

if __name__ == '__main__':
    root = Tk()
    application = DrawingApp(root)
    root.mainloop()
