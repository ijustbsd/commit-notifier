"""
Add tg_chat_id to Person
"""

from yoyo import step

__depends__ = {}

steps = [
    step("ALTER TABLE person ADD COLUMN tg_chat_id VARCHAR(255) NULL"),
]
