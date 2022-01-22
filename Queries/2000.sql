Select 
CASE 
WHEN (Select COUNT("CD_MUN_SIT_BIOMETRICA") 
        FROM "perfil_eleitorado_2000.csv"
        Where "CD_MUN_SIT_BIOMETRICA" = '-3') = COUNT("CD_MUN_SIT_BIOMETRICA") THEN TRUE
ELSE FALSE
END AS "CD_MUN_SIT_BIOMETRICA", 
CASE
WHEN (Select COUNT("NR_ZONA") 
        FROM "perfil_eleitorado_2000.csv"
        Where "NR_ZONA" = '-1') = COUNT("NR_ZONA") THEN TRUE
ELSE FALSE
END AS "NR_ZONA",
CASE
WHEN (Select COUNT("CD_ESTADO_CIVIL") 
        FROM "perfil_eleitorado_2000.csv"
        Where "CD_ESTADO_CIVIL" = '-3') = COUNT("DS_ESTADO_CIVIL") THEN TRUE
ELSE FALSE
END AS "CD_ESTADO_CIVIL",
CASE
WHEN (Select COUNT("CD_FAIXA_ETARIA") 
        FROM "perfil_eleitorado_2000.csv"
        Where "CD_FAIXA_ETARIA" = '-3') = COUNT("CD_FAIXA_ETARIA") THEN TRUE 
ELSE FALSE
END AS "CD_FAIXA_ETARIA",
CASE
WHEN (Select COUNT("CD_GRAU_ESCOLARIDADE") 
        FROM "perfil_eleitorado_2000.csv"
        Where "DS_GRAU_ESCOLARIDADE" = '0') = COUNT("DS_GRAU_ESCOLARIDADE") THEN TRUE
ELSE FALSE 
END AS "CD_GRAU_ESCOLARIDADE"
FROM "perfil_eleitorado_2000.csv"


Select 
    Cast(Replace("ANO_ELEICAO", '"', '') AS varchar(20)) AS "ANO_ELEICAO",
    Cast(Replace("SG_UF", '"', '') AS varchar(20)) AS "SG_UF",
    Cast(Replace("CD_MUNICIPIO", '"', '') AS varchar(20)) AS "CD_MUNICIPIO",
    Cast(Replace("NM_MUNICIPIO", '"', '') AS varchar(100)) AS "NM_MUNICIPIO",
    Cast(Replace("CD_GENERO", '"', '') AS varchar(20)) AS "CD_GENERO",
    Cast(Replace("DS_GENERO", '"', '') AS varchar(20)) AS "DS_GENERO",
    Cast(Replace("CD_GRAU_ESCOLARIDADE", '"', '') AS varchar(20)) AS "CD_GRAU_ESCOLARIDADE",
    Cast(Replace("DS_GRAU_ESCOLARIDADE", '"', '') AS varchar(20)) AS "DS_GRAU_ESCOLARIDADE",
    Cast(Replace("QT_ELEITORES_PERFIL", '"', '') AS bigint) AS "QT_ELEITORES_PERFIL",
    Cast(Replace("QT_ELEITORES_BIOMETRIA", '"', '') AS bigint) AS "QT_ELEITORES_BIOMETRIA",
    Cast(Replace("QT_ELEITORES_DEFICIENCIA", '"', '') AS bigint) AS "QT_ELEITORES_DEFICIENCIA",
    Cast(Replace("QT_ELEITORES_INC_NM_SOCIAL", '"', '') AS bigint) AS "QT_ELEITORES_INC_NM_SOCIAL"
From "perfil_eleitorado_2000.csv"