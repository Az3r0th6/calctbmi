from pyscript import document

def calculate_bmi(event):
    # Get values from input fields
    weight_input = document.getElementById("weight")
    height_input = document.getElementById("height")
    
    try:
        weight = float(weight_input.value)
        height = float(height_input.value)
        
        if weight <= 0 or height <= 0:
            document.getElementById("bmi-value").innerText = "--"
            category_element = document.getElementById("bmi-category")
            category_element.innerText = "Por favor, ingresa valores positivos."
            category_element.className = "category"
            
            result_div = document.getElementById("result")
            result_div.classList.remove("hidden")
            result_div.classList.add("show")
            return

        # Calculate BMI
        imc = weight / (height ** 2)
        
        # Display result
        document.getElementById("bmi-value").innerText = f"{imc:.2f}"
        
        # Determine category
        category = ""
        category_class = ""
        
        if imc < 18.5:
            category = "Bajo peso"
            category_class = "underweight"
        elif 18.5 <= imc < 25:
            category = "Peso normal"
            category_class = "normal"
        elif 25 <= imc < 30:
            category = "Sobrepeso"
            category_class = "overweight"
        else:
            category = "Obesidad"
            category_class = "obese"
            
        category_element = document.getElementById("bmi-category")
        category_element.innerText = category
        category_element.className = f"category {category_class}"
        
        # Show result div with animation
        result_div = document.getElementById("result")
        result_div.classList.remove("hidden")
        # Trigger reflow isn't strictly necessary in PyScript DOM interaction in the same way, 
        # but adding the class works for the CSS transition.
        result_div.classList.add("show")

    except ValueError:
        document.getElementById("bmi-value").innerText = "--"
        category_element = document.getElementById("bmi-category")
        category_element.innerText = "Por favor, ingresa números válidos."
        category_element.className = "category"
            
        result_div = document.getElementById("result")
        result_div.classList.remove("hidden")
        result_div.classList.add("show")
