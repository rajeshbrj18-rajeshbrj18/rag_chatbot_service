from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    supabase_url: str = Field(..., env="SUPABASE_URL")
    supabase_anon_key: str = Field(..., env="SUPBASE_ANON_KEY")
    supabse_service_role_key: str = Field(...,env="SUPABASE_SERVICE_ROLE_KEY")

    ai_provider: Literal["gemini"] = Field(default="gemini", env="AI_PROVIDER")

    gemini_api_key: str = Field(...,env="GEMINI_API_KEY")
    gemini_chat_model: str = Field(default="gemini-3.5-flash-lite", env="GEMINI_CHAT_MODEL")
    gemini_embed_model: str = Field(default="gemini-embedding-001", env="GEMINI_EMBED_MODEL")

    environment: str = Field(default="development", env="ENVIRONMENT")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")


    default_top_k: int = Field(default=6)
    chunk_size: int = Field(default=400)
    chunk_overlap: int = Field(default=40)
    temperature: float = Field(default=0.1)
    embedding_dimensions: int = Field(default=1536)

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()

def get_settings() -> Settings:
    return settings

