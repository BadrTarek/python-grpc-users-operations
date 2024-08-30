
mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

phone_number_regex = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


def format_pydantic_errors(errors:list) -> list:
    formatted_errors = []
    for error in errors:
        loc = " -> ".join(map(str, error['loc']))
        msg = f"Error in field '{loc}': {error['msg']}."
        if 'ctx' in error:
            if 'given' in error['ctx']:
                msg += f" (Provided value: {error['ctx']['given']})"
            if 'limit_value' in error['ctx']:
                msg += f" (Expected limit: {error['ctx']['limit_value']})"
        formatted_errors.append(msg)
    return formatted_errors