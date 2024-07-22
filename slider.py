import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def lissajous_curve(A, B, a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y)
    plt.title(f'Lissajous Curve: A={A}, B={B}, a={a}, b={b}, δ={delta}')
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

interact(
    lissajous_curve,
    A=FloatSlider(min=0.1, max=5.0, step=0.1, value=1.0, description='A'),
    B=FloatSlider(min=0.1, max=5.0, step=0.1, value=1.0, description='B'),
    a=FloatSlider(min=1, max=10, step=1, value=1, description='a'),
    b=FloatSlider(min=1, max=10, step=1, value=1, description='b'),
    delta=FloatSlider(min=0, max=2 * np.pi, step=0.1, value=0, description='δ')
)
