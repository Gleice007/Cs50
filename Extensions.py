def get_media_type(file_name):
    # Dicionário de extensões e seus tipos de mídia correspondentes
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".bmp": "image/bmp",
        ".webp": "image/webp",
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".ogg": "audio/ogg",
        ".mp4": "video/mp4",
        ".avi": "video/x-msvideo",
        ".mov": "video/quicktime",
        ".mkv": "video/x-matroska",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".html": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
        ".json": "application/json",
        ".xml": "application/xml",
    }

 # Converte o nome do arquivo para minúsculas para comparação
    file_name_lower = file_name.lower()

    # Verifica cada extensão no dicionário
    for ext in media_types:
        if file_name_lower.endswith(ext):
            return media_types[ext]
    
    # Se nenhuma extensão corresponder, retorna o tipo padrão
    return "application/octet-stream"

def main():
    # Solicita o nome do arquivo ao usuário
    file_name = input("Digite o nome do arquivo: ")
    # Obtém o tipo de mídia do arquivo
    media_type = get_media_type(file_name)
    # Exibe o tipo de mídia
    print(f"O tipo de mídia do arquivo '{file_name}' é: {media_type}")

# Executa o programa se este arquivo for executado diretamente
if __name__ == "_main_":
    main()




    
    




