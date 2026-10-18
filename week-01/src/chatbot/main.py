"""
Main Module

This is the entry point of the chatbot application. It orchestrates the
conversation loop and ties together all the other modules.

Key Concepts:
- Main loop: The core logic that runs repeatedly until the user quits
- State management: Keeping track of the conversation history
- Error handling: Gracefully handling problems without crashing

Functional Programming Approach:
- We use a list to store conversation history (immutable operations)
- Each function has a single, clear responsibility
- We compose smaller functions to build larger behaviors
"""

from src.chatbot import ui
from src.chatbot.api import (
    create_client,
    create_system_message,
    get_chat_response,
)
from src.chatbot.models import ChatMessage
from src.settings import Settings


def should_quit(user_input: str) -> bool:
    """
    Check if the user wants to quit the conversation.

    Args:
        user_input: The user's message

    Returns:
        True if the user wants to quit, False otherwise

    This is a pure function - same input always gives same output.
    We check for common quit commands (case-insensitive).
    """
    quit_commands = {"quit", "exit", "bye", "goodbye"}
    return user_input.lower() in quit_commands


def run_conversation_loop() -> None:
    """
    Main conversation loop - the heart of the chatbot!

    This function:
    1. Sets up the OpenAI client
    2. Displays the welcome message
    3. Runs the conversation loop until the user quits
    4. Handles errors gracefully

    The conversation history is stored as a list of ChatMessage objects.
    We start with a system message to set the chatbot's personality.
    """

    # TODO: Create OpenAI client

    settings = Settings()
    client = create_client(settings)

    # TODO: Initialize conversation history
    # Instructions:
    # 1. Create a system message using create_system_message() (no parameters needed!)
    # 2. Create a list called 'conversation_history' with just the system message
    # 3. This list will grow as the conversation progresses
    #
    # Hint: conversation_history should be a List[ChatMessage] type

    conversation_history: list[ChatMessage] = [create_system_message()]

    ui.display_welcome()

    # TODO: Main conversation loop
    # This is the core of the chatbot - it runs until the user quits.
    while True:
        try:
            user_input = ui.get_user_input()

            # Check if user wants to quit
            if should_quit(user_input):
                ui.display_goodbye()
                break

            # Validate that input is not empty
            if not user_input:
                ui.display_error("Please enter a message!")
                continue

            # TODO: Create and store user message
            # Code here

            user_message = ChatMessage(
                role="user",
                content=user_input,
            )
            conversation_history.append(user_message)

            ui.display_loading()

            # TODO: Get AI response from OpenAI and display it
            # Code here

            assistant_message = get_chat_response(
                client,
                conversation_history,
                settings.OPENAI_MODEL,
            )

            conversation_history.append(assistant_message)

            ui.display_assistant_message(assistant_message.content)

        except KeyboardInterrupt:
            ui.display_goodbye()
            break
        except Exception as e:  # noqa: BLE001
            ui.display_error(f"An error occurred: {e}")
            continue


def main() -> None:
    """
    Entry point for the chatbot application.

    This function is called when you run: python -m src.chatbot.main
    It wraps the conversation loop with top-level error handling.
    """
    try:
        run_conversation_loop()
    except KeyboardInterrupt:
        # User pressed Ctrl+C - exit gracefully
        print("\n")  # New line after ^C
        ui.display_goodbye()
    except Exception as e:  # noqa: BLE001
        # Unexpected error - show it and exit
        ui.display_error(f"Fatal error: {e}")
        ui.display_system_message(
            "Please check your configuration and try again.", "red"
        )


# This is a Python idiom - code here only runs if this file is executed directly
# (not if it's imported as a module)
if __name__ == "__main__":
    main()
