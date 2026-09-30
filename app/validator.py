from .user_repo import get_user_by_email, get_user_by_username


def validate_registration(
    username,
    email,
    password,
    confirm_password
):
    if not username.strip():
        return "Username is required."

    if not email.strip():
        return "Email is required"

    

    if not password:
        return "Password is required"

    if not confirm_password:
        return "Please confirm your password"

    if password != confirm_password:
        return "Passwords do not match."


    existing_username = get_user_by_username(username.strip())
    
    if existing_username:
        return "Username already exists."

    existing_user_email = get_user_by_email(email.strip())

    if existing_user_email:
        return "Email already exists."

    return None