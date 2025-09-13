def identify_intent(text):
    text = text.lower()
    if any(kw in text for kw in ['add', 'sum', 'plus']):
        return 'add'
    elif any(kw in text for kw in ['subtract', 'minus', 'difference']):
        return 'subtract'
    elif any(kw in text for kw in ['multiply', 'product']):
        return 'multiply'
    elif any(kw in text for kw in ['divide', 'quotient']):
        return 'divide'
    elif "create user" in text:
        return 'create_user'
    elif "delete user" in text:
        return 'delete_user'
    elif "list users" in text:
        return 'list_users'
    else:
        return 'general'
