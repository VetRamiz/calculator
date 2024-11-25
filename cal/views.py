from django.shortcuts import render
from .models import Model1

def calculate_weight(request):
    weight = None
    results = []

    # Fetch all model instances to display on the initial load
    model_instances = Model1.objects.all()[:7]  # Ensure we only take the first seven records

    # Get the weight from the request if it's a POST request
    if request.method == 'POST':
        weight = float(request.POST.get('weight', 0))
        
        # Define the multipliers
        multipliers = [0.35, 0.55, 0.65, 0.75, 0.85, 0.93, 1.0]
        
        # Calculate weights for each model instance
        for i, instance in enumerate(model_instances):
            calculated_weight = round(weight * multipliers[i])  # Round to nearest integer
            results.append({
                'set_number': instance.set_number,
                'reps': instance.reps,
                'weight': calculated_weight,
                'min_in_w_o': instance.min_in_w_o
            })
    else:
        # Initial load with default weight
        for instance in model_instances:
            results.append({
                'set_number': instance.set_number,
                'reps': instance.reps,
                'weight': 0,  # Default weight for initial display
                'min_in_w_o': instance.min_in_w_o
            })

    return render(request, 'cal/calculate_weight.html', {'results': results, 'weight': weight})