"""Initial schema

Revision ID: 58b0a60c9438
Revises:
Create Date: 2024-08-25 11:34:08.106488

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '58b0a60c9438'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'launches',
        sa.Column('launch_id', sa.TEXT(), nullable=False),
        sa.Column('id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False
        ),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('launch_id'),
    )
    op.create_table(
        'missions',
        sa.Column('mission_id', sa.TEXT(), nullable=False),
        sa.Column('twitter', sa.TEXT(), nullable=True),
        sa.Column('website', sa.TEXT(), nullable=True),
        sa.Column('wikipedia', sa.TEXT(), nullable=True),
        sa.Column('id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False
        ),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('mission_id'),
    )
    op.create_table(
        'rockets',
        sa.Column('rocket_id', sa.TEXT(), nullable=False),
        sa.Column('wikipedia', sa.TEXT(), nullable=True),
        sa.Column('id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False
        ),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('rocket_id'),
    )
    op.create_table(
        'launch_links',
        sa.Column('mission_id', sa.TEXT(), nullable=False),
        sa.Column('article_link', sa.TEXT(), nullable=True),
        sa.Column('flickr_images', sa.ARRAY(sa.TEXT()), nullable=False),
        sa.Column('presskit', sa.TEXT(), nullable=True),
        sa.Column('reddit_campaign', sa.TEXT(), nullable=True),
        sa.Column('reddit_launch', sa.TEXT(), nullable=True),
        sa.Column('reddit_media', sa.TEXT(), nullable=True),
        sa.Column('reddit_recovery', sa.TEXT(), nullable=True),
        sa.Column('video_link', sa.TEXT(), nullable=True),
        sa.Column('wikipedia', sa.TEXT(), nullable=True),
        sa.Column('launch_uuid', sa.Uuid(), nullable=False),
        sa.Column('id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False
        ),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['launch_uuid'], ['launches.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('launch_uuid'),
        sa.UniqueConstraint('mission_id'),
    )


def downgrade() -> None:
    op.drop_table('launch_links')
    op.drop_table('rockets')
    op.drop_table('missions')
    op.drop_table('launches')