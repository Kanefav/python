import GameUtilities as func


if func.VerificarArqExistente('profile') == False:
    func.CriarArquivo('profile')
else:
    MainPersona = func.Persona.criar()
    func.StartGame(MainPersona)