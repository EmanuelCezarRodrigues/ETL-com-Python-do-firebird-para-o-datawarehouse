import fdb
import pyodbc
from datetime import datetime
# Configurar a conexão com o banco Firebird
firebird_conn = fdb.connect(dsn=r'SEU ARQUIVO FIREBIRD', user='USUÁRIO DO BANCO', password='SENHA')
firebird_cursor = firebird_conn.cursor()

# Definir a consulta SELECT
query = """
    SELECT 
        V.VEICCODIGOEXTEMP as Oidbem,
        '2' AS Estabelecimento,  -- Alterado para '2'
        V.VEICCODIGO AS Veiculo,
        J.JDATAABERTURA,
        J.JDATAFECHAMENTO,
        S.JFDataInicio,
        S.JFDatafim,
        F.FUNCNOME,
        S.JFODOMETRO,
        S.JFCONSUMO
    FROM JORNADA j
    LEFT JOIN JFUNCIONARIO s ON s.VEICCODIGO = j.VEICCODIGO AND s.JDATAABERTURA = j.JDATAABERTURA
    LEFT JOIN FUNCIONARIO f ON f.FUNCCODIGO = s.FUNCCODIGO
    INNER JOIN VEICULO v ON v.VEICCODIGO = j.VEICCODIGO
    WHERE v.VEICCODIGOEXTEMP NOT IN ('000000015732');
"""

# Executar a consulta SELECT no Firebird
firebird_cursor.execute(query)

# Recuperar os resultados
results = firebird_cursor.fetchall()

# Fechar a conexão do Firebird
firebird_conn.close()

# Configurar a conexão com o SQL Server
sql_server_conn = pyodbc.connect("Driver={SQL Server};Server=Servidor SQL Server;Database= NOME DO BANCO ;uid=USUARIO ;pwd=SENHA")
sql_server_cursor = sql_server_conn.cursor()

# Inserir os dados na tabela JornadaG3 no SQL Server

for row in results:
    oidbem, estabelecimento, veiculo, dataabertura, datafechamento, jfdatainicio, jfdatafim, nomefuncionario, jfodometro, jfconsumo = row



    # Usar MERGE para inserir ou atualizar registros na tabela, evitando duplicar os dados. Caso já exista os dados, não sera reinserido na tabela criada.
    sql_merge = """
        MERGE INTO [JornadaG3] AS target
        USING (SELECT ? AS OIDBEM, ? AS Estabelecimento, ? AS Veiculo, ? AS DataAbertura, ?  AS DataFechamento,  ? JFDataInicio, ? AS JFDataFim, ? AS NomeFuncionario, ? AS KmRodado, ? AS Consumo) AS source
        ON target.OIDBEM = source.OIDBEM AND target.Estabelecimento = source.Estabelecimento AND target.Veiculo = source.Veiculo AND target.JFDataInicio = source.JFDataInicio AND target.JFDataFim = source.JFDataFim
        WHEN NOT MATCHED THEN
            INSERT (OIDBEM, Estabelecimento, Veiculo, DataAbertura, DataFechamento, JFDataInicio, JFDataFim, NomeFuncionario, KmRodado, Consumo)
            VALUES (source.OIDBEM, source.Estabelecimento, source.Veiculo, source.DataAbertura, source.DataFechamento, source.JFDataInicio, source.JFDataFim, source.NomeFuncionario, source.KmRodado, source.Consumo);
    """
    sql_server_cursor.execute(sql_merge, oidbem, estabelecimento, veiculo, dataabertura, datafechamento, jfdatainicio,
                              jfdatafim, nomefuncionario, jfodometro, jfconsumo)

# Confirmar e fechar a conexão do SQL Server
sql_server_conn.commit()
sql_server_conn.close()
