from django.shortcuts import render

# Vista para la página de inicio
def index(request):
    return render(request, 'paginas/index.html')

# Vista para la página del carrito
def carrito(request):
    return render(request, 'paginas/carrito.html')

# Vista para la página de contacto
def contacto(request):
    return render(request, 'paginas/contacto.html')

# Vista para el producto 1
def producto1(request):
    return render(request, 'paginas/producto1.html')

# Vista para el producto 2
def producto2(request):
    return render(request, 'paginas/producto2.html')

# Vista para el producto 3
def producto3(request):
    return render(request, 'paginas/producto3.html')

# Vista para el producto 4
def producto4(request):
    return render(request, 'paginas/producto4.html')

# Vista para el producto 5
def producto5(request):
    return render(request, 'paginas/producto5.html')

# Vista para el producto 6
def producto6(request):
    return render(request, 'paginas/producto6.html')
