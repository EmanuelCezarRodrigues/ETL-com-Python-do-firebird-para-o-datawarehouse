
Automatização de ETL para Integração de Dados de Consumo de Combustível da Frota de Ônibus
Este projeto visa a automação completa do processo ETL (Extract, Transform, Load) para integrar os dados de consumo de combustível da frota de ônibus em um data warehouse da empresa. O cenário envolve a obtenção de dados de equipamentos de medição de consumo, hospedados em um banco de dados Firebird gerenciado por um provedor que requer acesso temporário.

Desafio Inicial:

O processo anterior exigia que um analista acessasse manualmente o banco de dados do provedor por meio do IBExpert em Firebird e extraísse os dados. Além disso, havia a necessidade de combinar esses dados com informações do ERP da empresa por meio do QlikView. Esse processo demorava consideravelmente e envolvia intervenção manual, incluindo análise e limpeza de dados.

Solução:

Para superar essas limitações, foi desenvolvido um programa em Python que automatiza todo o processo ETL da seguinte forma:

Extração de Dados: O programa se conecta diretamente ao banco de dados Firebird hospedado pelo provedor, eliminando a necessidade de acesso manual. Os dados de consumo de combustível são extraídos de forma eficiente.

Transformação dos Dados: O script Python inclui recursos para limpeza e transformação dos dados, identificando e tratando outliers e registros incompletos que poderiam afetar a análise. Esta etapa pode ser personalizada de acordo com os requisitos específicos da empresa.

Carga de Dados no Data Warehouse: Os dados transformados são inseridos diretamente na tabela do data warehouse da empresa. O script identifica automaticamente registros duplicados e não insere dados repetidos, garantindo a integridade e eficiência do processo.

Benefícios:

Automatização e Economia de Tempo: A automatização completa elimina a intervenção manual, economizando tempo considerável no processo de ETL.

Maior Precisão e Consistência: A automação reduz erros humanos e garante que os dados sejam tratados de forma consistente a cada execução.

Integração Perfeita com o Data Warehouse: Os dados são integrados diretamente no data warehouse, tornando-os imediatamente disponíveis para análise e relatórios.

Melhoria na Tomada de Decisão: A disponibilidade rápida de dados limpos e prontos para análise permite uma tomada de decisão mais informada e ágil.

Este projeto representa uma melhoria significativa na eficiência operacional e capacidade analítica da empresa. A automação do processo ETL não apenas economiza tempo, mas também garante a qualidade e integridade dos dados em todo o processo, fornecendo informações valiosas para a tomada de decisões estratégicas
