from pyscript import document

def calculate_bmi(event):
    # Get values from input fields
    weight_input = document.getElementById("weight")
    height_input = document.getElementById("height")
    age_input = document.getElementById("age")
    gender_input = document.getElementById("gender")
    
    try:
        weight = float(weight_input.value)
        height = float(height_input.value)
        age = float(age_input.value)
        gender_val = gender_input.value
        
        if weight <= 0 or height <= 0 or age <= 0:
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
        
        # Sex for formulas: 1 for male, 0 for female
        sex = 1 if gender_val == "male" else 0

        # Body Fat Percentage (Deurenberg formula)
        # BFP = (1.20 × BMI) + (0.23 × Age) - (10.8 × sex) - 5.4
        fat_pct = (1.20 * imc) + (0.23 * age) - (10.8 * sex) - 5.4
        
        # Skeletal Muscle Mass (Lee et al. formula)
        # SMM (kg) = 0.244 * weight + 7.8 * height - 0.098 * age + 6.6 * sex - 3.3
        muscle_kg = (0.244 * weight) + (7.8 * height) - (0.098 * age) + (6.6 * sex) - 3.3
        muscle_pct = (muscle_kg / weight) * 100

        # Display results
        document.getElementById("bmi-value").innerText = f"{imc:.2f}"
        document.getElementById("fat-value").innerText = f"{fat_pct:.1f}"
        document.getElementById("muscle-value").innerText = f"{muscle_pct:.1f}"
        
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
        result_div.classList.add("show")

    except ValueError:
        document.getElementById("bmi-value").innerText = "--"
        document.getElementById("fat-value").innerText = "--"
        document.getElementById("muscle-value").innerText = "--"
        category_element = document.getElementById("bmi-category")
        category_element.innerText = "Por favor, ingresa números válidos."
        category_element.className = "category"
            
        result_div = document.getElementById("result")
        result_div.classList.remove("hidden")
        result_div.classList.add("show")
