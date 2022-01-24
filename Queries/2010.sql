Select 
    Cast("2010" AS varchar(100)) AS "ANO_ELEICAO",
    Cast("AC" AS varchar(100)) AS "SG_UF",
    Cast("ACRELÂNDIA" AS varchar(100)) AS "MUNICIPIO",
    Cast("1120" AS varchar(100)) AS "CD_MUNICIPIO",
    Cast("8" AS varchar(100)) AS "NR_ZONA",
    Cast("FEMININO" AS varchar(100)) AS "GENERO",
    Cast("16 ANOS" AS varchar(100)) AS "FAIXA_ETARIA",
    Cast("ENSINO FUNDAMENTAL COMPLETO" AS varchar(100)) AS "GRAU_DE_ESCOLARIDADE",
    Cast("2" AS varchar(100)) AS "QTD_ELEITORES_NO_PERFIL"
From "perfil_eleitorado_2010.txt"