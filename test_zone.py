from pydantic import BaseModel, Field

# this won't work since PositiveInt takes precedence over the
# constraints defined in Field meaning they're ignored
class Model(BaseModel):
    foo: int = Field(..., ge=0.0, le=1.0)
