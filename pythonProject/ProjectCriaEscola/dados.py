def escolha_dados(selecao):
  from random import choice
  if selecao == "nomealuno":
     nomealuno =['João','Lucas','Pedro','Mateus','Davi','Arthur','Bernardo','Heitor','Rafael',
           'Miguel','Enzo','Ethan','Gabriel','Lucca','Benjamin','Nicolas','Guilherme',
           'Gustavo','Murilo','Felipe','Samuel','Henrique','Lorenzo','Vinicius','Joaquim',
           'Leonardo','Ryan','Ian','Antônio','Victor','Bruno','Carlos','Davi','Kaique',
           'Patrick','Igor','Diego','Alexandre','Mateus Henrique','Gustavo Henrique',
           'Enzo Gabriel','Luiz Miguel','Felipe','Lucas Gabriel','Pedro Henrique',
           'Leonardo','Vinicius','Vicente','Eduardo','Fillipi','Abigail','Adeline',
           'Agatha','Alaina','Alejandra','Alexandra','Alice','Alicia','Amelia','Ana',
           'Andrea','Angela','Anna','Anne','Ariana','Arianna','Aurora','Beatrice','Bella',
           'Bernadette','Bethany','Bianca','Bonnie','Brenda','Briana','Brianna','Camilla',
           'Caroline','Cassandra','Catherine','Cecilia','Chloe','Christina','Claire','Clara',
           'Daisy','Danielle','Daphne','Deborah','Diana','Elizabeth','Emily','Emma','Eva','Fatima',
           'Gabriela','Gianna','Gracie','Helen','Ingrid','Irene','Isabel','Isabelle','Isis','Jennifer',
           'Jessica']

     nn = choice(nomealuno)
     return nn
  elif selecao == "sobrenome":
     sobrenome = [' Rodrigues', ' Almeida', ' Moreira', ' da Silva', ' dos Santos', ' Galdino', ' Kronemberger',
                  ' Martins',' Pereira', ' Cardoso', ' Gonçalves', ' Lima', ' Freitas', ' Ribeiro', ' Marques',
                  ' Ferreira']
     ss = choice(sobrenome)
     return ss
  elif selecao == "email":
     email = ('@hotmail.com', '@gmail.com', '@yahoo.com.br', '@zoho.com')
     ee = choice(email)
     return ee
  elif selecao == "nomeinstrutor":
     nomeinstrutor = ['Celestina','Icaro','Ava','Ravi','Alba','Zion','Noah','Caleb','Liam','Gael','Elon','Ayla',
                      'Zoe','Aurora','Tito','Nina','Mabel','Pilar','Sam','Caetana','Nara','Rael','Ubaldo']
     return nomeinstrutor
  elif selecao == "cursos":
     cursos = ['Técnico em Administração','Técnico em Agronegócio','Técnico em Análises Clínicas','Técnico em Automação Industrial',
               'Técnico em Construção Naval','Técnico em Desenvolvimento de Sistemas','Técnico em Edificações','Técnico em Eletrônica',
               'Técnico em Enfermagem','Técnico em Estética','Técnico em Gastronomia','Técnico em Informática','Técnico em Logística',
               'Técnico em Mecânica','Técnico em Nutrição e Dietética','Técnico em Produção Áudio e Vídeo','Técnico em Próteses Dentárias',
               'Técnico em Radiologia','Técnico em Recursos Humanos','Técnico em Redes de Computadores','Técnico em Saúde Bucal',
               'Técnico em Segurança do Trabalho','Técnico em Veterinária']
     return cursos
  elif selecao == "certificados":
     certificados = ['Certificação ITIL','Certificação CISSP','Oracle Certified Professional Advanced PL/SQL',
                     'Certificação DELL EMC','VMware VCP-Cloud','Certificações MCSD','CCIE','Certificação PMP',
                     'AWS Certified Solutions Architect – Associate','Certified in the Governance of Enterprise IT (CGEIT)']
     cc = choice(certificados)
     return cc
  elif selecao == "horainstrutor":
     horainstrutor = ['10','12','15']
     hh = choice(horainstrutor)
     return hh
  elif selecao == "precocurso":
     precocurso = [120,160,200]
     pp = choice(precocurso)
     return pp
  else:
      return 0