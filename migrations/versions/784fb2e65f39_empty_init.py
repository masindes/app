"""Empty Init

Revision ID: 784fb2e65f39
Revises: 9d6f3ea71cee
Create Date: 2024-12-14 13:21:34.529508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '784fb2e65f39'
down_revision: Union[str, None] = '9d6f3ea71cee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
