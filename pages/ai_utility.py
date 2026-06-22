import ollama


def ai_heal(page_source:str, broken_locator: str, selector_type:str):

    truncated_html = page_source[:6000]
    # prompt = f"""
    # You are an expert QA Automation Engineer.
    # An automated test failed because the selector '{broken_locator}' could not be found, the selector type is {selector_type}
    # Check the current webpage"s HTML and find the closest match for the {broken_locator}.
    # Analyze the following snippet of the webpage's current HTML and find the correct, updated CSS selector for that element.
    
    # HTML:
    # {truncated_html}
    
    # Instructions:
    # - Respond with ONLY the raw CSS selector string (e.g., #submit-button or button.btn-primary).
    # - Do not include any explanations, markdown code blocks, backticks, or conversational text.
    # """
    prompt = f"""
    You are an expert QA Automation Engineer specializing in DOM analysis and selector repair.
    
    CONTEXT:
    - A test failed because the locator '{broken_locator}' (Type: {selector_type}) could not be found.
    - Your goal is to find the correct CSS selector for the *same* element in the provided HTML snippet.
    
    TASK:
    1. Analyze the provided HTML snippet.
    2. Identify the element that corresponds to '{broken_locator}'.
       - If {selector_type} is 'xpath', mentally convert the logic to find the target element.
    
    CRITICAL RULES FOR SELECTOR GENERATION:
    - **PRIORITY 1 (ID):** If the target element has an `id` attribute, the selector MUST be ONLY `#id-value`. 
      - DO NOT add the tag name (e.g., do NOT write `input#id-value`).
      - DO NOT add other attributes.
      - Example: If ID is "login", return `#login`, NOT `input#login`.
    - **PRIORITY 2 (Class):** If no ID exists, use the most specific class or combination (e.g., `button.btn-primary`).
    - **PRIORITY 3 (Attributes):** Use other attributes only if ID and Class are missing.
    
    HTML SNIPPET:
    {truncated_html}

    OUTPUT RULES:
    - Respond with ONLY the raw CSS selector string.
    - Do NOT include markdown code blocks (no ```css).
    - Do NOT include explanations, backticks, or conversational text.
    - If no matching element is found, return "NOT_FOUND".
    """

    try:
        print(f"broken locator : {broken_locator}")
        response = ollama.chat(
            model = "llama3.2",
            messages = [{"role": "user", "content": prompt}]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        print("Can't communicate with the model")
        return broken_locator    
