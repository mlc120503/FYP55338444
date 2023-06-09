def name_general(data):
    # rename with dict
    data['grad'].replace({'香港大学': 'HKU', 'The University of Hong Kong': 'HKU', 'HK': 'HKU', '[HKU': 'HKU',
                          'Hong Kong University': 'HKU',
                          '[HKU];MIEE': 'HKU', '香港科技大学': 'HKUST',
                          'The Hong Kong University of Science & Technology': 'HKUST',
                          'The Hong Kong University of Science and Technology': 'HKUST',
                          '香港城市大学': 'CityU', 'City University of Hong Kong': 'CityU', 'CityU HK': 'CityU',
                          'CityU (HK)': 'CityU', 'CPHK': 'CityU',
                          '香港理工大学': 'PolyU', 'PolyUH.K.': 'PolyU', 'PolyU (HK)': 'PolyU', '[PolyUH.K.': 'PolyU',
                          'PolyU HK': 'PolyU', '香港理工学院': 'PolyU',
                          'The Hong Kong Polytechnic University': 'PolyU',
                          '香港中文大学': 'CUHK', 'The Chinese University of Hong Kong': 'CUHK', 'CU HK': 'CUHK',
                          '香港浸会大学': 'HKBU',
                          'Hongyi SUN': 'Aalborg University',
                          'Univ of Wisconsin': 'University of Wisconsin-Madison',
                          '威斯康星大学': 'University of Wisconsin-Madison',
                          'Case Western Reserve U,Boston': 'Boston University', 'CMU': 'Carnegie Mellon University',
                          '波士顿大学': 'Boston University',
                          'Carnegie Mellon': 'Carnegie Mellon University', 'Xidian': 'Xidian University',
                          'Tsinghua': 'Tsinghua University', '清华大学': 'Tsinghua University',
                          'NTHU': 'Tsinghua University',
                          'ANU': 'The Australian National University',
                          '澳大利亚国立大学': 'The Australian National University',
                          'Illinois Inst Tech': 'Illinois Institute of Technology', 'McMaster': 'McMaster University',
                          'Uppsala': 'Uppsala University', 'University of Cambridge': 'Cambridge',
                          'Cambridge, UK': 'Cambridge', 'Cantab': 'Cambridge',
                          '剑桥大学': 'Cambridge', '英国剑桥大学': 'Cambridge',
                          'New South Wales': 'University of New South Wales',
                          'UNSW': 'University of New South Wales', '新南威尔士大学': 'University of New South Wales',
                          'U of Waterloo': 'University of Waterloo', '- UWaterloo': 'University of Waterloo',
                          'Waterloo': 'University of Waterloo', 'CWRU': 'Case Western Reserve University',
                          'Sydney': 'The University of Sydney', 'Sydney Uni': 'The University of Sydney',
                          '悉尼大学': 'The University of Sydney',
                          'University of Toronto': 'Toronto', 'UToronto': 'Toronto',
                          'Melbourne': 'The University of Melbourne', 'National University of Singapore': 'NUS',
                          '新加坡国立大学': 'NUS',
                          'National Univ. of Singapore': 'NUS',
                          'Montfort大学': 'De Montfort University', '北京航空航天大学': 'Beihang University',
                          'Massachusetts Institute of Technology': 'MIT',
                          '麻省理工学院': 'MIT',
                          '美国麻省理工学院': 'MIT',
                          'Massachusetts': 'MIT',
                          '美国乔治亚理工学院': 'Georgia Institute of Technology',
                          '年乔治亚理工学院': 'Georgia Institute of Technology',
                          '格斯大学': 'Rutgers University', '普利茅斯大学': 'University of Plymouth',
                          'UBC': 'The University of British Columbia',
                          'BritishColumbia': 'The University of British Columbia',
                          'NTU': 'Nanyang Technological University',
                          'NTU Singapore': 'Nanyang Technological University',
                          '南洋理工大学': 'Nanyang Technological University',
                          '新加坡南洋理工大学': 'Nanyang Technological University',
                          'ZJU': 'Zhejiang University', '浙江大学': 'Zhejiang University',
                          'EPFL': 'The École polytechnique fédérale de Lausanne',
                          'UMD': 'University of Maryland, College Park',
                          'Liverpool': 'University of Liverpool',
                          '利物浦大学': 'University of Liverpool', '东南大学': 'Southeast University',
                          'The University of Maryland': 'University of Maryland, College Park',
                          'Maryland': 'University of Maryland, College Park', 'McGill': 'McGill University',
                          '麦吉尔大学': 'McGill University', '昆明理工大学': 'Kunming University of Science and Technology',
                          'UCLA': 'University of California, Los Angeles',
                          '加州大学洛杉矶分校': 'University of California, Los Angeles',
                          'PKU': 'Peking University', '北京大学': 'Peking University',
                          'UMN': 'University of Minnesota Twin Cities', '布朗大学': 'Brown University',
                          'University of Minnesota': 'University of Minnesota Twin Cities',
                          'USC': 'University of Southern California',
                          '南加州大学': 'University of Southern California',
                          '(BME) USC': 'University of Southern California',
                          'Linkoping, Sweden': 'Linköping University',
                          'Univ. of Southern California': 'University of Southern California',
                          'OSU': 'The Ohio State University', 'Auckland': 'The University of Auckland',
                          '奥克兰大学': 'The University of Auckland',
                          'Kansas State': 'Kansas State University', 'Yale': 'Yale University',
                          'Illinois': 'University of Illinois at Urbana-Champaign',
                          'the University of Illinois at Urbana-Champaign': 'University of Illinois at Urbana-Champaign',
                          'UIUC': 'University of Illinois at Urbana-Champaign',
                          'Harvard, Illinois': 'University of Illinois at Urbana-Champaign',
                          '伊利诺伊大学': 'University of Illinois at Urbana-Champaign',
                          'University of Illinois Urbana-Champaign': 'University of Illinois at Urbana-Champaign',
                          'University of Illinois, Urbana-Champaign': 'University of Illinois at Urbana-Champaign',
                          'Texas A&M': 'Texas A&M University', '德州农工大学': 'Texas A&M University',
                          'TAMU': 'Texas A&M University', 'UMich': 'University of Michigan-Ann Arbor',
                          'University of Michigan': 'University of Michigan-Ann Arbor',
                          'Princeton': 'Princeton University', 'Glasgow': 'University of Glasgow',
                          'Cincinnati': 'University of Cincinnati', 'Harvard': 'Harvard University',
                          'Harv.': 'Harvard University',
                          '哈佛大学': 'Harvard University',
                          '(ECE) GaTech': 'Georgia Institute of Technology',
                          'Georgia Tech': 'Georgia Institute of Technology',
                          'Sunderland': 'University of Sunderland', 'RMIT': 'RMIT University',
                          'London': 'Imperial College London', '伦敦帝国理工学院': 'Imperial College London',
                          'Lond': 'Imperial College London', 'Lond.': 'Imperial College London',
                          '帝国理工学院': 'Imperial College London', '。帝国理工学院': 'Imperial College London',
                          'Western Ontario': 'Western University',
                          'Washington in Saint Louis': 'Washington University in St. Louis',
                          'Wales': 'University of Wales', '伯明翰大学': 'University of Birmingham',
                          'Iowa State': 'Iowa State University',
                          'Iowa State Univ.': 'Iowa State University',
                          'Berkeley': 'University of California, Berkeley',
                          '加利福尼亚大学': 'University of California, Berkeley',
                          'UC Berkeley': 'University of California, Berkeley',
                          'Duke': 'Duke University', 'Indiana University': 'Indiana University Bloomington',
                          'Indiana': 'Indiana University Bloomington',
                          'Indiana Univ., Bloomington': 'Indiana University Bloomington',
                          'Victoria': 'University of Victoria',
                          'University of Victoria, Canada': 'University of Victoria',
                          'Columbia University': 'Columbia', 'Columbia Univ.': 'Columbia',
                          'Col.': 'Columbia', '哥伦比亚大学': 'Columbia',
                          'Columbia University in The City of New York': 'Columbia',
                          'KAUST': 'King Abdullah University of Science & Technology',
                          'UTD': 'University of Texas at Dallas', 'UTDallas': 'University of Texas at Dallas',
                          'Dallas': 'University of Texas at Dallas', 'UCSB': 'University of California, Santa Barbara',
                          'UC Santa Barbara': 'University of California, Santa Barbara',
                          'California': 'University of California, Santa Barbara',
                          'UT Austin': 'The University of Texas at Austin',
                          'Texas': 'The University of Texas at Austin',
                          '德克萨斯大学': 'The University of Texas at Austin',
                          'Lehigh': 'Lehigh University', 'University of Bern, Switzerland': 'University of Bern',
                          'IST/Technical University of Lisbon, Portugal': 'University of Lisbon',
                          'Laval': 'Université Laval',
                          'UTC': 'University of Technology of Compiegne',
                          'Manchester': 'The University of Manchester', '曼彻斯特大学': 'The University of Manchester',
                          'UMIST': 'The University of Manchester',
                          'Caltech': 'California Institute of Technology',
                          '加州理工学院': 'California Institute of Technology',
                          'Loughborough': 'Loughborough University',
                          'Pennsylvania State': 'Pennsylvania State University', 'NYU': 'New York University',
                          'The Pennsylvania State University': 'Pennsylvania State University',
                          'Polytech. Inst. Of NY': 'New York University', 'Stanford University': 'Stanford',
                          '斯坦福大学': 'Stanford', 'Purdue': 'Purdue University',
                          '普渡大学': 'Purdue University', '莱斯大学': 'Rice University',
                          'the University of Arizona': 'The University of Arizona',
                          'Cornell': 'Cornell University', '成功大学': 'National Cheng Kung University',
                          'UC San Diego': 'University of California, San Diego',
                          'University of California San Diego': 'University of California, San Diego',
                          '加州大学': 'University of California, San Diego',
                          '宾夕法尼亚大学': 'University of Pennsylvania', 'Pennsylvania': 'University of Pennsylvania',
                          '瑞士联邦理工学院': 'ETH Zurich', '密苏里大学': 'University of Missouri, Columbia',
                          'University of Missouri': 'University of Missouri, Columbia',
                          '科迪亚大学': 'Concordia University',
                          'Concordia': 'Concordia University', '中国科学院自动化研究所': 'Chinese Academy of Sciences',
                          '中国科学院': 'Chinese Academy of Sciences',
                          '[ChineseAcademyofSciences': 'Chinese Academy of Sciences', '鲁汶大学': 'KU Leuven',
                          '牛津大学': 'University of Oxford',
                          'Oxford': 'University of Oxford', 'Oxon': 'University of Oxford',
                          'University Grenoble Alpes': 'Université Grenoble Alpes',
                          'University of Massachusetts': 'University of Massachusetts Amherst',
                          'UMASS at Amherst': 'University of Massachusetts Amherst',
                          '马萨诸塞大学': 'University of Massachusetts Amherst',
                          '弗吉尼亚理工大学': 'Virginia Polytechnic Institute and State University',
                          'Wollongong': 'University of Wollongong', '[Wollongong': 'University of Wollongong',
                          '悉尼科技大学': 'University of Technology Sydney',
                          'Pavia, Italy': 'Università degli Studi di Pavia', 'Notre Dame': 'University of Notre Dame',
                          'Tokyo': 'The University of Tokyo', '东京大学': 'The University of Tokyo',
                          'Washington': 'University of Washington',
                          'North Carolina, Chapel Hill': 'University of North Carolina at Chapel Hill',
                          'Alberta': 'University of Alberta', 'USTC': 'University of Science and Technology of China',
                          '佛罗里达大学': 'University of Florida', '博洛尼亚大学': 'University of Bologna',
                          '萨里大学': 'University Of Surrey', '西北大学': 'Northwestern University',
                          '华中科技大学': 'Huazhong University of Science and Technology',
                          '东京技术学院': 'Tokyo Institute of Technology',
                          '巴黎综合理工学院': 'Ecole Polytechnique', '理工学院大学': 'Ecole Polytechnique',
                          '新墨西哥大学': 'University of New Mexico',
                          '查尔姆斯理工大学': 'Chalmers University of Technology',
                          'WashingtonState': 'Washington State University',
                          '州立大学': 'Washington State University',
                          'NPU': 'Northwestern Polytechnical University',
                          'NorthwesternPolytechnical': 'Northwestern Polytechnical University',
                          'uOttawa': 'University of Ottawa', 'D.Litt.': 'Vrije Universiteit Amsterdam',
                          'SimonFraser': 'Simon Fraser University', 'LaTrobe': 'La Trobe University',
                          'FloridaAtlantic': 'Florida Atlantic University', 'Southampton': 'University of Southampton',
                          'JohnsHopkins': 'Johns Hopkins University', "Xi'anJiaotong": 'Xi’an Jiaotong University',
                          'SBU': 'Stony Brook University', 'Nanjing': 'Nanjing University',
                          'NEU': 'Northeastern University', '帕多瓦大学': 'Università di Padova',
                          '上海交通大学': 'Shanghai Jiao Tong University',
                          'MichiganState': 'Michigan State University',
                          'IITRoorkee': 'Indian Institute of Technology Roorkee',
                          '斯特拉思克莱德大学': 'University of Strathclyde', '巴斯大学': 'University of Bath',
                          '莫纳什大学': 'Monash University', '纳什大学': 'Monash University',
                          '贝尔法斯特女王大学': "Queen's University Belfast",
                          '伦敦城市大学': 'City, University of London',
                          '蒙特利尔综合理工学院': 'Université de Montréal',
                          '伦敦大学': 'UCL', 'University College London': 'UCL',
                          '北京理工学院': 'Beijing Institute of Technology',
                          'RUC': 'Roskilde University', '[RUC': 'Roskilde University',
                          '英国伦敦大学': 'Queen Mary University of London',
                          'Northumbria': 'Northumbria University at Newcastle', 'Tasmania': 'University of Tasmania',
                          'Univ. of Sheffield': 'The University of Sheffield', 'Leeds': 'University of Leeds',
                          'UQ': 'The University of Queensland', '中山大学': 'Sun Yat-sen University'
                          }, inplace=True)
