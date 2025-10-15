#6th
def sms_len(text) -> str:
    try:
        return str(text)[:160]
    except:
        return 'Data error'