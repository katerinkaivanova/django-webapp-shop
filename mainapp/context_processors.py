def basket(request):
    print(f'context processor basket works')

    if request.user.is_authenticated:
        return {
            'basket': request.user.basket.all()
        }
    else:
        return {
            'basket': []
        }
