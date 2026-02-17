import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def validate_patch(target: Any, attribute: str) -> bool:
    """
    Checks if the target object has the specified attribute.
    Returns True if valid, False otherwise.
    """
    if not hasattr(target, attribute):
        logger.warning(f"Patch validation failed: '{target}' has no attribute '{attribute}'")
        return False
    return True

def apply_patch(target: Any, attribute: str, new_value: Any, validate: bool = True) -> bool:
    """
    Applies a monkey patch to the target object.
    
    Args:
        target: The object to patch (e.g., a class or module).
        attribute: The name of the attribute to patch (str).
        new_value: The new value (e.g., function) to assign.
        validate: If True (default), checks if the attribute exists before patching.
                  If validation fails, the patch is skipped.
    
    Returns:
        True if the patch was applied, False otherwise.
    """
    if validate and not validate_patch(target, attribute):
        logger.warning(f"Skipping patch for {target.__name__ if hasattr(target, '__name__') else target}.{attribute}")
        return False

    try:
        setattr(target, attribute, new_value)
        logger.info(f"Successfully patched {target.__name__ if hasattr(target, '__name__') else target}.{attribute}")
        return True
    except Exception as e:
        logger.error(f"Failed to apply patch to {attribute}: {e}")
        return False
