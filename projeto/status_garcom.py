from dados import garcons

def alterar_status_garcom(id, status):
    # Valida se o status é válido
    if status not in ['disponivel', 'ocupado', 'em_atendimento', 'turno_encerrado']:
        raise ValueError('Status inválido. Use: disponivel, ocupado, em_atendimento ou turno_encerrado')
    
    # Valida se o garçom existe
    if id not in garcons:
        raise ValueError(f'Garçom com ID {id} não encontrado')
    
    # Altera o status
    garcons[id]['status'] = status
    
    return f"Status do garçom {garcons[id]['nome']} alterado para '{status}'"