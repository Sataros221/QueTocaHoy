class Subject:
    # HARDCODED SUBJECTS
    ####################
    THIRD_YEAR: dict[str, str] = {
        "1": "Ingenieria de Software I",
        "2": "Programacion Web",
        "3": "Redes de Computadoras",
        "4": "Taller de Base de Datos",
        "5": "Probabilidades y Estadistica",
        "6": "Teoria Sociopolitica",
        "7": "Programacion para Moviles",
        "8": "Practica Profesional",
    }
    FORTH_YEAR: dict[str, str] = {
        "1": "Inteligencia Artificial II",
        "2": "Seminario Profesional",
        "3": "Gestion de Software",
        "4": "Web Semantica",
        "5": "Redes LAN",
        "6": "Ciencia de Datos",
    }
    # mutual_subjects = ["Profesor Guia", "Evento"]
    # THIRD_YEAR.extend(mutual_subjects)
    # FORTH_YEAR.extend(mutual_subjects)

    def get_subjects(self, year: int) -> list[str]:
        """
        Returns the subjects of a course by selecting the year of studies (for example: 3rd year, 4th year)

        Example:
        >>> # input
        >>> 3
        >>> # output
        >>> "Matematica", "Estadistica", "Ing. Software", etc..

        >>> # input
        >>> 4
        >>> # output
        >>> "Inteligencia Artificial II", "Gestion de Software", etc..
        """

        match year:
            case 3:
                return self.THIRD_YEAR
            case 4:
                return self.FORTH_YEAR
            case _:
                raise Exception(f"Year not allowed: {year}")
