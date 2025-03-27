import uvicorn
from dotenv import load_dotenv
import os
from cursor_integration import app

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    uvicorn.run(
        "cursor_integration:app",
        host=host,
        port=port,
        reload=True
    )