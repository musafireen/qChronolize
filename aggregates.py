from qChronolyze import sameVrsIndicator

from aggregates_test import *


jinn_iblis_dhurriya = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "*rr", 
                    "strTyp": "root",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
]

jinn_iblis = [
    *jinn_iblis_dhurriya,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

iblis_shaytan = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
                },
                {
                    "stri": "wEd", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 45
        },
    ],
]

iblis_nar = [
    [
        {
            "strL": [
                {
                    "stri": "naAr",
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
]

iblis_malak = [
    [
        {
            "strL": [
                {
                    "stri": "malak", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<iboliys",
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
]

iblis = [
    *iblis_nar,
    *iblis_malak,
    *jinn_iblis,
]

jinn_malak = [
    *iblis_malak,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
]

untha_dua_shirk = [
    [
        {
            "strL": [
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
                {
                    "stri": "dEw",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "duwn", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 11
        },
    ],
]

lat_uzza_manat_untha_ism = [
    [
    {
      "wrdDis": 75,
      "strL": [
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
                {
                    "stri": "smw", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
                },
        { "stri": goddess, "strTyp":"lem",  "flt": "",},
                {
                    "stri": "A^baA'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "Znn", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
                },
                {
                    "stri": "hwy", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
                },
      ],
    },
  ]
    for goddess in ["{ll~a`t","{loEuz~aY`","manaw`p"]
]

lat_uzza_manat_untha_ism_malak = [
    [
    {
      "wrdDis": optO[0]["wrdDis"],
      "strL": optO[0]["strL"] + [ {"stri": "malak","strTyp": "lem",},]
    },
  ]
    for optO in lat_uzza_manat_untha_ism
]

malak_tasmiya_untha = [
    *lat_uzza_manat_untha_ism_malak,
    # [
    #     {
    #         "strL": [
    #             {
    #                 "stri": "malak",
    #                 "strTyp": "lem",
    #             },
    #         ],
    #         "wrdDis": 20,
    #     },
    # ],
]

tasmiya_untha = [
    # *lat_uzza_manat_untha_ism,
    *lat_uzza_manat_untha_ism_malak,
]

ism_liqab = [
        [
    {
      "wrdDis": 10,
      "strL": [
                {
                    "stri": "smw", 
                    "strTyp": "root",
                    # "poSp": "N",
                    # "frm": "ii"
                },
                {
                    "stri": "lqb", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
                {
                    "stri": "fsq", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
      ],
    },
  ],
]

# ism_jdl = [
#         [
#     {
#       "wrdDis": 10,
#       "strL": [
#                 {
#                     "stri": "smw", 
#                     "strTyp": "root",
#                     "poSp": "V",
#                     "frm": "ii"
#                 },
#                 {
#                     "stri": "jdl", 
#                     "strTyp": "root",
#                     # "frm": "ii"
#                 },
#       ],
#     },
#   ],
# ]

tasmiya_abd = [
    # *malak_tasmiya_untha,
        [
    {
      "wrdDis": 20,
      "strL": [
                {
                    "stri": "A^baA'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "smw", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii"
                },
                {
                    "stri": "Ebd", 
                    "strTyp": "root",
                    # "frm": "ii"
                },
      ],
    },
  ],
        [
    {
      "wrdDis": 10,
      "strL": [
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                },
                {
                    "stri": "smw", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii"
                },
      ],
    },
  ],
    
]

tasmiya_abd_malak_untha = [
    *malak_tasmiya_untha,
    *tasmiya_untha,
    *tasmiya_abd,
]

malak_banat = [
    [
        {
            "strL": [
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
                {
                    "stri": "malak",
                    "strTyp": "lem",
                },
                {
                    "stri": "banaAt", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 50,
        },
    ],
]

malak_untha = [
    *malak_tasmiya_untha,
    *malak_banat,
    [
        {
            "strL": [
                {
                    "stri": "malak",
                    "strTyp": "lem",
                },
                {
                    "stri": ">unvaY`", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20,
        },
    ],

]

malak_ism = [
    *malak_tasmiya_untha,
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jiboriyl", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "miykaY`l", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ma`lik2", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ha`ruwt", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ma`ruwt", "strTyp": "lem",},
      ],
    },
  ],
]

malak_khazanah_zabaniya = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "z~abaAniyap", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": 20,
      "strL": [
        { "stri": "xazanat", "strTyp": "lem",},
        { "stri": "jan~ap", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": 20,
      "strL": [
        { "stri": "xazanat", "strTyp": "lem",},
        { "stri": "jahan~am", "strTyp": "lem",},
      ],
    },
  ],
]

malak_mala = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mala>", "strTyp": "lem",},
        { "stri": ">aEolaY`", "strTyp": "lem",},
      ],
    },
  ],
]

malak_jund = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { "stri": "lam", "strTyp": "lem",},
        { "stri": "rAy", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "wrdDis": 1,
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { "stri": "rab~", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": 4,
      "strL": [
        { "stri": "jund", "strTyp": "lem",},
        { "stri": "samaA^'", "strTyp": "lem",},
      ],
    },
  ],
]

malak_janah = [
        [
    {
      "wrdDis": 10,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "janaAH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_rasul = [
            [
    {
      "wrdDis": 5,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "jEl", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "wrdDis": 4,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "nzl", "strTyp": "root",},
      ],
    },
  ],
          [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rasuwl", "strTyp": "lem",},
        { "stri": "Sfw", "strTyp": "root",},
      ],
    },
  ],
]

malak_ruh = [
        [
    {
      "wrdDis": 11,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_amr = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "laA", "strTyp": "lem",},
        { "stri": "ESy", "strTyp": "root",},
        { "stri": "Amr", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "wrdDis": 11,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": ">amor", "strTyp": "lem",},
        { "stri": "ruwH", "strTyp": "lem",},
      ],
    },
  ],
]

malak_arsh = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Hml", "strTyp": "root",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hml", "strTyp": "root",},
        { "stri": "Earo$", "strTyp": "lem",},
      ],
    },
  ],
]

malak_muqarrab = [
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "muqar~abuwn", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": 5,
      "strL": [
        { "stri": "muqar~abuwn", "strTyp": "lem",},
        { "stri": "Eil~iy~iyn", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "muqar~abuwn", "strTyp": "lem",},
      ],
    },
  ],
]

malak_rabb_akhadh = [
            [
    {
      "wrdDis": 3,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "rab~", "strTyp": "lem",},
        { "stri": "Ax*", "strTyp": "root",},
      ],
    },
  ],
]

malak_shafaah = [
    [
      {
        "wrdDis": 10,
        "strL": [
          { "stri": "malak", "strTyp": "lem",},
          { "stri": "$afa`Eap", "strTyp": "lem",},
        ],
      }
        
    ]
]

jinnah_malak_maqam_saff = [
  [
      
        {
          "wrdDis": 70,
          "strL": [
            { "stri": "malak", "strTyp": "lem",},
            { "stri": "jin~ap", "strTyp": "lem",},
            { "stri": "S~aA^f~uwn", "strTyp": "lem",},
          ],
        },

  ],
  [

      {
        "wrdDis": 70,
        "strL": [
          { "stri": "malak", "strTyp": "lem",},
          { "stri": "jin~ap", "strTyp": "lem",},
          { "stri": "maqaAm", "strTyp": "lem",},
        ],
      },
    ],
]


malak_qabil = [
                [
            {
                "strL": [
                    {
                        "stri": "qabiyl",
                        "strTyp": "lem",
                        "frm": "All",
                    },
                    {
                        "stri": "malak",
                        "strTyp": "lem",
                    },
                ],
            },
        ],
]

malak = [
  *jinn_malak,
  *malak_ism,
  *malak_untha,
  *malak_khazanah_zabaniya,
  *malak_mala,
  *malak_jund,
  *malak_rasul,
  *malak_ruh,
  *malak_amr,
  *malak_arsh,
  *malak_muqarrab,
  *malak_rabb_akhadh,
  *malak_shafaah,
  *malak_janah,
  *jinnah_malak_maqam_saff,
  *malak_qabil,
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "Erj", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "mdd", "strTyp": "root",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "strTyp": "lem",},
        { "stri": "sbH", "strTyp": "root",},
      ],
    },
  ],
  #     [

  #     {
  #     "wrdDis": 20,
  #       "strL": [
  #         { "stri": "malak", "strTyp": "lem",},
  #         { "stri": "jan~ap", "strTyp": "lem",},
  #       ],
  #     },

  # ]
]

# malak = list(set(malak))

angels = malak

shaytan_qabil = [
                [
            {
                "strL": [
                    {
                        "stri": "qabiyl",
                        "strTyp": "lem",
                        "frm": "All",
                    },
                    {
                        "stri": "$ayoTa`n",
                        "strTyp": "lem",
                    },
                ],
            },
        ],
]

qabil = [
    malak_qabil,
    shaytan_qabil,
]

shaytan_mareed_dua_shirk = [
    [
        {
            "strL": [
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "dEw",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "m~ariyd", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "duwn", 
                #     "strTyp": "lem",
                # },
            ],
            "wrdDis": 16
        },
    ],
]

shaytan_mareed = [
    *shaytan_mareed_dua_shirk,
        [
        {
            "strL": [
                # {
                #     "stri": "tbE",
                #     "strTyp": "root",
                #     # "poSp": "V",
                # },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "m~ariyd", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

shaytan_sam_srq_sama_buruj = [
    [
        {
            "strL": [
                {
                    "stri": "samoE", 
                    "strTyp": "lem",
                },
                {
                    "stri": "buruwj", 
                    "strTyp": "lem",
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "rajiym", 
                    "strTyp": "lem",
                },
                {
                    "stri": "srq",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30,
        },
    ],
    
]

shaytan_zyn_dun = [
    [
        {
            "strL": [
                {
                    "stri": "duwn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "zyn",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 5,
        },
    ],
    
]

shaytan_marid_sama_dunya_kawkab = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "kawokab", 
                    "strTyp": "lem",
                },
                {
                    "stri": "d~unoyaA", 
                    "strTyp": "lem",
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "m~aArid", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20,
        },
    ],
]

shaytan_maarid = [
    *shaytan_marid_sama_dunya_kawkab,   
]

shaytan_abd = [
    [
        {
            "strL": [
                {
                    "stri": "Ebd",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
            #     {
            #         "stri": "<ila`h", 
            #         "strTyp": "lem",
            #     },
            ],
            "wrdDis": 5,
        },
    ],
]

shaytan_akhi_bdhr = [
    [
        {
            "strL": [
                {
                    "stri": ">ax",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "b*r",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ], 
]
shaytan_mani = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "mny",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "ii",
                },
            ],
            "wrdDis": 10
        },
    ],
]

shaytan_nabi_tamanna_ilqa_naskh_fitna = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "mny",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "ftn",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
                },
                {
                    "stri": "nsx",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
                },
                {
                    "stri": "lqy",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
                },
                {
                    "stri": "n~abiY~", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ], 
]

shaytan_amr_btk_anam_adhan = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "btk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": ">u*unN",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "n~aEam", 
                    "strTyp": "lem",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ],    
]

shaytan_amr_ghayr_khalq = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "gyr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "xaloq",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
]

shaytan_amr_munkar = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "munkar",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
]

shaytan_amr_sayyiah = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "suw^'",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "say~i}ap",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "say~i_#aAt",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
]

shaytan_amr_fahisha = [
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "faHo$aA^'",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
    [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "fa`Hi$ap",
                    "strTyp": "lem",
                    # "poSp": "V",
                },
                {
                    "stri": "Amr",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 30
        },
    ], 
]

shaytan_amr = [
    *shaytan_amr_ghayr_khalq,
    *shaytan_amr_btk_anam_adhan,
    *shaytan_amr_fahisha,
    # [
    #     {
    #         "strL": [
    #             {
    #                 "stri": "Amr",
    #                 "strTyp": "root",
    #                 # "poSp": "V",
    #             },
    #             {
    #                 "stri": "$ayoTa`n", 
    #                 "strTyp": "lem",
    #             },
    #         ],
    #         "wrdDis": 30
    #     },
    # ],
]

shaytan_shirk = [
    *shaytan_mareed_dua_shirk,
    *shaytan_abd,
    [
        {
            "strL": [
                {
                    "stri": "TwE",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
            "wrdDis": 30
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "tbE",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
            "wrdDis": 30
        },
    ],
]

shaytan_sharik_awlad = [
    [
        {
            "strL": [
                # {
                #     "stri": "jin~",
                #     "strTyp": "lem",
                # },
                {
                    "stri": "$rk",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "iii"
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "maAl", 
                #     "strTyp": "lem",
                # },
                {
                    "stri": "walad", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 10
        },
    ],
]

shaytan_why = [
    [
        {
            "strL": [
                # {
                #     "stri": "jin~",
                #     "strTyp": "lem",
                # },
                {
                    "stri": "wHy",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                # {
                #     "stri": "<ins", 
                #     "strTyp": "lem",
                # },
                # {
                #     "stri": "waliY~", 
                #     "strTyp": "lem",
                # },
            ],
            "wrdDis": 10
        },
    ],
]

# jinn_qarin = [
#         [
#         {
#             "strL": [
#                 {
#                     "stri": "jin~",
#                     "strTyp": "lem",
#                 },
#                 {
#                     "stri": "qariyn", 
#                     "strTyp": "lem",
#                 },
#             ],
#             "wrdDis": 20
#         },
#     ],
# ]

shaytan_qarin = [
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "ri}aA^'", 
                    "strTyp": "root",
                },
            ],
            "wrdDis": 25
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "E$w", 
                    "strTyp": "root",
                },
            ],
            "wrdDis": 25
        },
    ],
]

qarin = [
    # *jinn_qarin,
    *shaytan_qarin,
    [
        {
            "strL": [
                {
                    "stri": "qariyn", 
                    "strTyp": "lem",
                },
            ],
            # "wrdDis": 25
        },
    ],
]

shaytan_muqarran = [
        [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "m~uqar~aniyn", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
]

shaytan_wiswas = [
        [
        {
            "strL": [
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "wsws",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
                },
            ],
            "wrdDis": 20
        },
    ],
]

shaytan = [
    *shaytan_sam_srq_sama_buruj,
    *shaytan_maarid,
    *shaytan_mareed,
    *shaytan_qarin,
    *shaytan_muqarran,
    *shaytan_sharik_awlad,
    *shaytan_shirk,
    *shaytan_akhi_bdhr,
    *shaytan_mani,
    *shaytan_amr,
    *shaytan_why,
    *shaytan_wiswas,
    *shaytan_qabil,
    *iblis,
]

# shaytan = list(set(shaytan))

muqarran = [
    *shaytan_muqarran,
        [
        {
            "wrdDis": sameVrsIndicator,
            "strL": [
                {
                    "stri": "m~uqar~aniyn", 
                    "strTyp": "lem",
                },
            ],
        },
    ],
]

qarin_muqarran = [
    *qarin,
    *muqarran,
]

kahin_majnun = [
        [
        {
            "strL": [
                {
                    "stri": "majonuwn",
                    "strTyp": "lem",
                },
                {
                    "stri": "kaAhin", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
]

ifrit_jinn = [
        [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Eiforiyt", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],
]

ifrit = [
    *ifrit_jinn,
]

jinna_wiswas = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap", 
                    "strTyp": "lem",
                },
                {
                    "stri": "wsws",
                    "strTyp": "root",
                    # "poSp": "V",
                    # "frm": "ii",
                },
            ],
            "wrdDis": 20
        },
    ],
]

wiswas = [
    jinna_wiswas,
    *shaytan_wiswas,
]

jinn_sama_mss_qEd_sam = [
    [
        {
            "strL": [
                {
                    "stri": "jin~", 
                    "strTyp": "lem",
                },
                {
                    "stri": "samoE", 
                    "strTyp": "lem",
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "lms",
                    "strTyp": "root",
                    # "poSp": "V",
                },
                {
                    "stri": "qEd",
                    "strTyp": "root",
                    # "poSp": "V",
                },
            ],
            "wrdDis": 75,
        },
    ],
]

jinn_rasul_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "rasuwl", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 10
        },
    ], 
]

jinn_ins_ummah_khala = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": ">um~ap", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
                {
                    "stri": "xlw", 
                    "strTyp": "root",
                    "poSp": "V",
                },
            ],
            "wrdDis": 10
        },
    ], 
]

jinn_ins_nfdh_sama = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "samaA^'", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
                {
                    "stri": "nf*", 
                    "strTyp": "root",
                    "poSp": "V",
                },
            ],
            "wrdDis": 10
        },
    ], 
]

jinn_ins_abd = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Ebd", 
                    "strTyp": "root",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 10
        },
    ],
]

jinn_ins_dll = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
                {
                    "stri": "Dll", 
                    "strTyp": "root",
                    "poSp": "V",
                },
            ],
            "wrdDis": 5
        },
    ], 
]

jinn_wHy_ins_shaytan = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "wHy",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 10
        },
    ],
]

jinn_wHy_ins = [
    *jinn_wHy_ins_shaytan,  
]

jinn_shaytan = [
    *jinn_wHy_ins_shaytan,
]

jinn_sharik_kharaq_bani = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                    # "poSp": "N",
                    # "frm": "i",
                },
                {
                    "stri": "xrq", 
                    "strTyp": "root",
                },
                {
                    "stri": "banaAt", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 35
        },
    ],    
]

jinn_sharik = [
    *jinn_sharik_kharaq_bani,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ariyk", 
                    "strTyp": "lem",
                    # "poSp": "N",
                    # "frm": "i",
                },
            ],
            "wrdDis": 35
        },
    ], 
]

jinn_abd = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Ebd", 
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "i"
                },
                {
                    "stri": ">akovar",
                    "strTyp": "lem",
                },
                {
                    "stri": "malak",
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 15
        },
    ],
]

jinna_nasab = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "nsb", 
                    "strTyp": "root",
                },
            ],
            "wrdDis": 20
        },
    ],
]

jinnah_nas_khannas = [
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "n~aAs", 
                    "strTyp": "lem",
                },
                {
                    "stri": "xan~aAs", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
    
]

jinnah_khannas = [
    *jinnah_nas_khannas,
]

khannas = [
    *jinnah_nas_khannas,
    [
        {
            "strL": [
                {
                    "stri": "xan~aAs", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
]

jinn_wali_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "wly", 
                    "strTyp": "root",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 7
        },
    ],
]

jinn_awdh_ins = [
        [
        {
            "strL": [
                {
                    "stri": "Ew*", 
                    "strTyp": "root",
                },
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 25
        },
    ],
]

jinn_istikthar_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "kvr",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

jinn_tayr = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "Tayor", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

jinn_ijtima_ins = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "jmE",
                    "strTyp": "root",
                    "poSp": "V",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

jinn_shirk = [
    *jinna_wiswas,
    *jinn_ijtima_ins,
    *jinn_istikthar_ins,
    *jinn_wHy_ins_shaytan,
    *jinn_wali_ins,
    *jinn_awdh_ins,
    *jinn_sharik,
    *jinn_abd,
    *jinna_nasab,
    *jinn_sharik_kharaq_bani
]

jinn_ins_jahannam = [
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "jahan~am",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
                {
                    "stri": "jahan~am",
                    "strTyp": "lem",
                },
                {
                    "stri": "n~aAs", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

jann_ins_Tmth = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins",
                    "strTyp": "lem",
                },
                {
                    "stri": "Tmv",
                    "strTyp": "root",
                },
            ],

        },
    ],   
]

jinn_ins = [
    *jinn_wali_ins,
    *jinn_awdh_ins,
    *jinn_istikthar_ins,
    *jinn_ijtima_ins,
    *jinn_wHy_ins_shaytan,
    *jinn_ins_jahannam,
    *jinnah_nas_khannas,
    *jinn_ins_nfdh_sama,
    *jinn_ins_dll,
    *jinn_ins_ummah_khala,
    *jinn_rasul_ins,
    *jann_ins_Tmth,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
                {
                    "stri": "<ins", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

jann_dhanb = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "*anb",
                    "strTyp": "lem",
                },
            ],

        },
    ],   
]

jann_nar = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "naAr",
                    "strTyp": "lem",
                },
            ],

        },
    ],   
]

jann_hzz = [
    [
        {
            "strL": [
                {
                    "stri": "jaA^n~",
                    "strTyp": "lem",
                },
                {
                    "stri": "hzz",
                    "strTyp": "root",
                },
            ],

        },
    ],   
]

jinn = [
    *kahin_majnun,
    *jinn_malak,
    *ifrit_jinn,
    # *jinn_qarin,
    *jinn_iblis,
    *jinn_shaytan,
    *jinn_ins,
    *jinn_tayr,
    *jinn_shirk,
    *jann_nar,
    *jann_dhanb,
    *jann_hzz,
    [
        {
            "strL": [
                {
                    "stri": "jin~",
                    "strTyp": "lem",
                },
            ],

        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jin~ap",
                    "strTyp": "lem",
                },
            ],

        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "majonuwn",
                    "strTyp": "lem",
                },
            ],
        },
    ],
    [
        {
            "strL": [
                {
                    "stri": "jnn",
                    "strTyp": "root",
                    "poSp": "V",
                    "frm": "i",
                },
            ],
        },
    ],
]

# jinn = list(set(jinn))

jinn_shaytan = [
    *jinn,
    *shaytan,
]

kahin_shair = [
    [
        {
            "strL": [
                {
                    "stri": "kaAhin", 
                    "strTyp": "lem",
                },
                {
                    "stri": "$aAEir",
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 20
        },
    ],
]

kahin = [
    *kahin_majnun,
    *kahin_shair,

]


evil_spirits = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "(?:devil|[^d]evil|demon|shaitaan)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<iboliys", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bls", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jin~", "flt": "(?:[jJ]inn)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jin~ap", "flt": "(?:[Jj]inn|mad)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnn", "flt": "(?:^mad$|mad man|madman|surely mad)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jaAn~", "flt": "(?:snake|jinn)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hyy", "flt": "snake",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qrn", "flt": "companion",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "qrn", "flt": "",},
      ],
    },
  ],
      [
        {
            "strL": [
                {
                    "stri": "<iboliys",
                    "strTyp": "lem",
                },
                {
                    "stri": "$ayoTa`n", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnn", "flt": "jinn",},
        { "stri": "$Tn", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mrd", "flt": "rebellious",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Eiforiyt", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "mss", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnd", "flt": "(?:host|troop|force)",},
        { "stri": "<iboliys", "flt": "(?:iblis|devil|satan)",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "wly", "flt": "(?:ally|allies|guardian|protector|friend)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "Ebd", "flt": "",},
        { "stri": "laA", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "Anv", "flt": "",},
        { "stri": "dEw", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "qrn", "flt": "",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnn", "flt": "(?:jinn)",},
        { "stri": "dwn", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnn", "flt": "(?:jinn)",},
        { "stri": "$rk", "flt": "",},
      ],
    },
  ],
]


magic = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "poetry",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "hair",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "Sirius",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "monument",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "(?:symbol|rite)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "poet(?!r)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sHr", "flt": "magic(?!i)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sHr", "flt": "magician",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sHr", "flt": "(?<!they )bewitched",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sHr", "flt": "(?:they bewitch|you bewitch|delude)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "baAbil", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jbt", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfv", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "khn", "flt": "",},
      ],
    },
  ],
]

ruh = [
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amiyn", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "Erj", "strTyp": "root", "flt": "",},
        { "stri": "yawom", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
        { "stri": "qwm", "strTyp": "root", "flt": "",},
        { "stri": "yawom", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "malak", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "qds", "strTyp": "root", "flt": "",},
        { "stri": "nzl", "strTyp": "root", "flt": "",},
        { "stri": "vbt", "strTyp": "root", "flt": "",},
        { "stri": "Amn", "strTyp": "root", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "qds", "strTyp": "root", "flt": "",},
        { "stri": "Ayd", "strTyp": "root", "flt": "",},
        { "stri": "EiysaY", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "EiysaY", "strTyp": "lem", "flt": "",},
        { "stri": "glw", "strTyp": "root", "flt": "",},
      ],
      "lbl": "ruh isa"
    },
  ],
    [
    {
      "wrdDis": 10,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "Ayd", "strTyp": "root", "flt": "",},
        { "stri": "<iyma`n", "strTyp": "root","poSp": "N","frm": "iv",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "wHy", "strTyp": "root", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "lqy", "strTyp": "root", "flt": "",},
        { "stri": ">amor", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
    [
    {
      "wrdDis": 12,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "nfx", "strTyp": "root", "flt": "",},
        { "stri": "ba$ar", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ بشر"
    },
    {
      "wrdDis": 14,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "nfx", "strTyp": "root", "flt": "",},
        { "stri": "<insa`n", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ إنسان"
    },
  ],
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "nfx", "strTyp": "root", "flt": "",},
        { "stri": "faroj", "strTyp": "lem", "flt": "",},
      ],
      "lbl": "روح نفخ مريم"
    },
  ],
    [
    {
      "wrdDis": 12,
      "strL": [
        { "stri": "ruwH", "strTyp": "lem", "flt": "",},
        { "stri": "rsl", "strTyp": "root", "flt": "",},
        { "stri": "maroyam", "strTyp": "lem", "flt": "",},
      ],
    },
  ],
]

nafs = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfs", "flt": "(?:soul|self)",},
      ],
    },
  ],
]

spirits = [
    *ruh,

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfx", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Suwr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Swr", "flt": "",},
      ],
    },
  ],

]

spirituals = [
        *angels,
        *evil_spirits,
        *ruh,
]

isa = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "masiyH", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "EiysaY", "flt": "isa",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "maryam", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yaHoyaY`", "flt": "yahya",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zakariy~aA", "flt": "zakariya",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "EimoraAn", "flt": "imran",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kalimap", "flt": "(?:word|.*)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kalaAm", "flt": "(?:word|.*)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Tayor", "flt": "(?:bird)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mahod", "flt": "bed",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fTr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ftr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "muwsaY`", "flt": "musa",},
      ],
    },
  ],
]


idols_base = [
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "wad~", "strTyp":"lem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "manaw`p", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "baEol2", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "ma`lik2", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "suwaAE", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "yaEuwq", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "nasor", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "T~a`guwt", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],    
]


idols = [
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "wad~", "strTyp":"lem", "flt": "wadd",},
        { "stri": "wdd", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lwt", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lwy", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{ll~a`t", "strTyp":"lem",  "flt": "",},
        { "stri": "lyt", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
        { "stri": "Ezz", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "{loEuz~aY`", "strTyp":"lem",  "flt": "",},
        { "stri": "Ezw", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "manaw`p", "strTyp":"lem",  "flt": "",},
        { "stri": "mny", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "baEol2", "strTyp":"lem",  "flt": "",},
        { "stri": "bEl", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "ma`lik2", "strTyp":"lem",  "flt": "malik",},
        { "stri": "mlk", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "suwaAE", "strTyp":"lem",  "flt": "",},
        { "stri": "swE", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
        { "stri": "gyv", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "yaguwv", "strTyp":"lem",  "flt": "",},
        { "stri": "gwv", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "yaEuwq", "strTyp":"lem",  "flt": "",},
        { "stri": "Ewq", "strTyp":"root", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "nasor", "strTyp":"lem",  "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "T~a`guwt", "strTyp":"lem",  "flt": "",},
        { "stri": "Tgy", "strTyp":"root", "flt": "",},
      ],
    },
  ],
]

heavenlies = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kwkb", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "njm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$ms", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qmr", "flt": "",},
      ],
    },
  ],
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "[Ss]irius",},
      ],
    },
  ],

]

shirk2 = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$rk", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mu$orik", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<ila`h", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "a`lihap", "flt": "",},
      ],
    },
  ],
]

rituals = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wvn", "flt": "idol",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Snm", "flt": "idol",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "nuSob", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "naSab", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "n~aASibap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuSub", "strTyp": "stem", "flt": "",},
        { "stri": "nSb", "strTyp": "root", "poSp": "V", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "naSiyb", "strTyp": "stem", "flt": "",},
        { "stri": "jEl", "strTyp": "root", "flt": "assign",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "saA^}ibap", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "waSiylap", "strTyp": "stem", "flt": "",},
        { "stri": "wSl", "strTyp": "root", "poSp":"V", "frm": "i", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "waSiylap", "strTyp": "stem", "flt": "",},
        { "stri": "wSl", "strTyp": "root", "poSp":"V", "frm": "ii", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": 77430,
      "strL": [
        { "stri": "baHor", "strTyp": "stem", "flt": "",},
        { "stri": "baHiyrap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HaAm", "strTyp": "stem", "flt": "",},
        { "stri": "Hamiy~ap", "strTyp": "stem", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HaAm", "strTyp": "stem", "flt": "",},
        { "stri": "Hmy", "strTyp": "root", "poSp": "V", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": ">azolaAm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hrm", "flt": "",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xlS", "flt": "",},
        { "stri": "bTn", "flt": "",},
        { "stri": "*kr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "[Pp]oet(?!r)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "(?:[Pp]oetry)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ma$oEar", "strTyp": "lem", "flt": "",},
        { "stri": "$Er", "strTyp": "root", "poSp":"V", "frm": "i", "flt": "(?:[Hh]air)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$aAEir", "strTyp": "lem", "flt": "(?:[Ss]ymbol|rite)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$iEor", "strTyp": "lem", "flt": "(?:[Mm]onument)",},
      ],
    },
  ],
            [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Er", "flt": "[Ss]irius",},
      ],
    },
  ],
]


ilah_dun_baEd = [
    [
        {
            "strL": [
                # {
                #     "stri": "Ax*",
                #     "strTyp": "root",
                #     # "poSp": "V",
                # },
                {
                    "stri": "duwn", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ila`h", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
    [
        {
            "strL": [
                # {
                #     "stri": "Ax*",
                #     "strTyp": "root",
                #     # "poSp": "V",
                # },
                {
                    "stri": "baEod", 
                    "strTyp": "lem",
                },
                {
                    "stri": "<ila`h", 
                    "strTyp": "lem",
                },
            ],
            "wrdDis": 30
        },
    ],
]

shirk = [
    
    *idols,
    # *heavenlies,
    # *shirk2,
    *rituals,
    *evil_spirits,

        [
    {
      "wrdDis": 1,
      "strL": [
        { "stri": "Alh", "flt": "(?:^((?!Allah).)*$)",},
        { "stri": "dwn", "flt": "(?:other|esides|exclud|Us|instead)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Alh", "flt": "(?:^((?!Allah).)*$)",},
        { "stri": "Axr", "flt": "",},
        { "stri": "maEa", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ebd", "flt": "(?:worship|serv)",},
        { "stri": "dwn", "flt": "(?:other|esides|exclud|Us|instead)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dEw", "flt": "",},
        { "stri": "maEa", "flt": "",},
        { "stri": "AHd", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dEw", "flt": "(?:^((?!caller).)*$)",},
        { "stri": "dwn", "flt": "(?:other|esides|exclud|Us|instead)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "Alh", "flt": "(?:^((?!Allah).)*$)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "dwn", "flt": "",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "(?:^((?!we).)*$)", "strTyp": "root",  "frm": "viii", },
        { "stri": "wld", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wld", "flt": "(?:begot|beget)",},
        { "stri": "Alh", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wld", "flt": "",},
        { "stri": "sbH", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "lam", "flt": "",},
        { "stri": "wld", "flt": "(?:begot|beget)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "SHb", "flt": "(?:wife)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<an~aY", "flt": "",},
        { "stri": "wld", "flt": "(?:son)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<an~aY", "flt": "",},
        { "stri": "SaAHibap", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "malak", "flt": "(?:[Aa]ngel)",},
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ax*", "flt": "",},
        { "stri": "bny", "flt": "(?:[Dd]aughter)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jEl", "flt": "assign",},
        { "stri": "bny", "flt": "(?:[Dd]aughter)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xrq", "flt": "",},
        { "stri": "bny", "flt": "(?:[Ss]on|[Ss]hild|[Dd]aughter)",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$ariyk", "flt": "",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjd", "flt": "",},
        { "stri": "A^dam", "flt": "",},
        { "stri": "malak", "flt": "(?:[Aa]ngel)",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kwkb", "flt": "star",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kwkb", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "njm", "flt": "",},
        { "stri": "nZr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "sjd", "flt": "",},
        { "stri": "dwn", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$ms", "flt": "",},
        { "stri": "sjd", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qmr", "flt": "",},
        { "stri": "rab~", "flt": "",},
        { "stri": "ha`*aA", "flt": "",},
      ],
    },
  ],
        
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rhb", "flt": "",},
        { "stri": "rbb", "flt": "",},
        { "stri": "Ax*", "flt": "(?:taken)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hbr", "flt": "",},
        { "stri": "rbb", "flt": "",},
        { "stri": "Ax*", "flt": "(?:taken)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mlk", "flt": "(?:[Aa]ngel)",},
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "rbb", "flt": "(?:[Ll]ords)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nbA", "flt": "",},
        { "stri": "Ax*", "flt": "", "strTyp": "root",  "frm": "viii", },
        { "stri": "rbb", "flt": "(?:[Ll]ords)",},
      ],
    },
  ],


        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jzA", "flt": "",},
        { "stri": "Ebd", "flt": "",},
      ],
    },
  ],

]

places = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SafaA", "flt": "safa",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "marowap", "flt": "marwa",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "siyniyn", "flt": "sin",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qurayo$", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tub~aE", "flt": "tubba",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "saba<", "flt": "saba",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "misor", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ruwm", "flt": "rom",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ramaDaAn", "flt": "ramadan",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "EarafaAt", "flt": "arafa",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bak~ap", "flt": "bakka",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bador", "flt": "badr",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yavorib", "flt": "yathrib",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "makkap", "flt": "makka",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kaEobap", "flt": "ka",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hunayon", "flt": "hunayn",},
      ],
    },
  ],
]

animals = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nml", "flt": "ant",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qrd", "flt": "(?:monkey|ape)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nHl", "flt": "bee",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Tyr", "flt": "bird",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "TaA}ir", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ejl", "flt": "calf",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jml", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bEr", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nwq", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<ibil", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "hym", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "E$r", "flt": "camel",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bqr", "flt": "(?:heifer|cow)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "grb", "flt": "(?:raven|crow)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "klb", "flt": "(?:dog|hound)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hmr", "flt": "(?:donkey|ass)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fyl", "flt": "elephant",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nEj", "flt": "ewe",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hwt", "flt": "fish",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "*bb", "flt": "(?:fly|flies)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "DfdE", "flt": "frog",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mEz", "flt": "goat",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "hdhd", "flt": "hoopoe",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xyl", "flt": "(?:horse|cavalry)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jwd", "flt": "steed",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qml", "flt": "lice",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qsr", "flt": "lion",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jrd", "flt": "locust",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bED", "flt": "mosquito",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fr$", "flt": "moth",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bgl", "flt": "mule",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xnzr", "flt": "(?:pig|swine)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "slw", "flt": "quail",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "gnm", "flt": "sheep",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "vEb", "flt": "(?:serpent|snake)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hyy", "flt": "(?:serpent|snake)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jaAn~", "flt": "(?:snake|serpent|jinn)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Enkb", "flt": "spider",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "*#b", "flt": "wolf",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nEm", "flt": "(?:cattle|livestock)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bhm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dbb", "flt": "(?:creature|animal|beast)",},
      ],
    },
  ],
]

hindi = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "msk", "flt": "musk",},
      ],
    },
  ],
]

geez = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hwr", "flt": "disciple",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zrb", "flt": "",},
      ],
    },
  ],
]

copt_gypt = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xtm", "flt": "seal",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "taAbuwt", "flt": "(?:ark|chest|.*)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Tgy", "flt": "(?:idol|deit|god|evil)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jbt", "flt": "(?:copt|gypsy|superstition)",},
      ],
    },
  ],
]

latin = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sij~iyl", "flt": "clay",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjl", "flt": "scroll",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qnTr", "flt": "(?:centenarium|heap|wealth|store)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dnr", "flt": "(?:denarius|coin)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qmS", "flt": "shirt",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qSr", "flt": "(?:castle|palace|fort)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SrT", "flt": "(?:path|way)",},
      ],
    },
  ],
]

greek = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qsTs", "flt": "balance",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qrTs", "flt": "parchment",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "drhm", "flt": "dirham",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qld", "flt": "key",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qld", "flt": "garland",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qlm", "flt": "(?:pen|reed|cane)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sTr", "flt": "(?:story|tale)",},
      ],
    },
  ],
]

syr_christ = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nHs", "flt": "(?:copper|bronze|brass|smoke)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "krs", "flt": "throne",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Abb", "flt": "(?:pasture|grass)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ajr", "flt": "(?:reward)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbl", "flt": "(?:way|path)",},
      ],
    },
  ],
]

aram_jew = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jlw", "flt": "exile",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbt", "flt": "(?:sabbath|rest)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbT", "flt": "(?:tribe|descendants|scepter|rod|stick)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "safarap", "flt": "scribe",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sfr", "flt": "book",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rbb", "flt": "(?:the rabbis|worshipper)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rib~iy~uwn", "flt": "(?:scholar)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bhm", "flt": "(?:beast|quadruped)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Sdq", "flt": "charity",},
      ],
    },
  ],
]

akkadian = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fxr", "flt": "pottery",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": ">asowaAq", "flt": "market",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "swq", "flt": "(?:leg|shin|stem)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "frt", "flt": "(?:sweet|fresh)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "swr", "flt": "(?:bracelet|fetter|chain)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "k#s", "flt": "cup",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sunodus", "flt": "silk",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sTr", "flt": "(?:writ)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sTr", "flt": "(?:control)",},
      ],
    },
  ],
]

farsi = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fyl", "flt": "elephant",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fxr", "flt": "boast",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fwj", "flt": "(?:group|company|.*)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "srj", "flt": "(?:lamp|.*)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": ">abaAriyq", "flt": "(?:jug)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Efr", "flt": "strong",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tan~uwr", "flt": "oven",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnh", "flt": "(?:blame|sin)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnd", "flt": "(?:host|troop|army|force)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "srd", "flt": "link",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "srdq", "flt": "wall",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "firodaws", "flt": "paradise",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mjs", "flt": "mag",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "srbl", "flt": "(?:trouser|pants|garment)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kaAfuwr", "flt": "(?:camphor|kafur)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zanjabiyl", "flt": "(?:ginger|zanjabil)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "barozax", "flt": "barrier",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "knz", "flt": "(?:treasure|hoard)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<isotibraq", "flt": "(?:brocade|silk)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ebqr", "flt": "carpet",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "namaAriq", "flt": "cushion",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ark", "flt": "(?:couch|throne)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zmhr", "flt": "cold",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "m$j", "flt": "mix",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mzj", "flt": "mix",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wzr", "flt": "(?:minister|assist|bear|burden|refuge)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Er$", "flt": "(?:erect|construct|roof|throne|trellis)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dwl", "flt": "(?:circul|alter)",},
      ],
    },
  ],
]


nabis = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "A^dam", "flt": "(?:Adam|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuwH", "flt": "(?:Nuh|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<idoriys", "flt": "(?:Idris|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "huwd", "flt": "(?:Hud|)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ewd", "flt": "Aad",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SaAliH", "flt": "(?:Salih)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "vamuwd", "flt": "Thamud",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tub~aE", "flt": "Tubba",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": ">ayokap", "flt": "wood",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ras~", "flt": "(?:rass|Raas)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hijor", "flt": "(?:the Rocky Tract)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<iram", "flt": "(?:Aram|Iram)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<iboraAhiym", "flt": "(?:Ibrahim|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "luwT", "flt": "(?:Lut)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<isoma`Eiyl", "flt": "(?:Ishmael|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<isoHaAq", "flt": "(?:Isaac|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yaEquwb", "flt": "(?:Yaqub|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yuwsuf", "flt": "(?:Yusuf|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": ">ay~uwb", "flt": "(?:Ayyub|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$uEayb", "flt": "(?:Shuaib|)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "madoyan", "flt": "(?:Midian|Madyan)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "muwsaY`", "flt": "(?:Musa|)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "firoEawon", "flt": "(?:Pharaoh|Firaun)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ha`ruwn", "flt": "(?:Harun|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "TaAluwt", "flt": "(?:Saul|Talut)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jaAluwt", "flt": "(?:Goliath|Jalut)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "daAwud", "flt": "(?:Dawood|Dawud|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sulaymaAn", "flt": "(?:Sulaiman|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kifol", "flt": "(?:Kifl)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nuwn", "flt": "(?:Nun)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yuwnus", "flt": "(?:Yunus)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<iloyaAs", "flt": "(?:Elijah|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yasaE", "flt": "(?:Elisha)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qrn", "flt": "(?:Qarnain)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Euzayor", "flt": "(?:Uzair)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "luqomaAn", "flt": "(?:Luqman)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zakariy~aA", "flt": "(?:Zakariya|)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "yaHoyaY", "flt": "(?:Yahya)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "maroyam", "flt": "(?:Mary)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "EiysaY", "flt": "isa",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Aibn", "flt": "son",},
        { "stri": "maryam", "flt": "Mary",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "muHam~ad", "flt": "(?:Muhammad|)",},
      ],
    },
  ],
]

islam_iman = [

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(?:believer|believing|who believe|\(will\) believe)", "strTyp": "root",  "frm": "iv",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(?:faith|belief)", "strTyp": "root",  "frm": "iv",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "[tT]rustworthy", "strTyp": "root",  "frm": "i",  "poSp": "ADJ", },
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "[tT]rustworthy", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(safe|secure)", "strTyp": "root",  "frm": "i",  "poSp": "ADJ", },
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(safely|safe(?!ty)|secure)", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(?:security)", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "(?:trust)", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "place of safety", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "", "strTyp": "root",  "frm": "viii", },
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "slm", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<isolaAm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "musolim", "flt": "(?:submissive|submit|surrender|Muslim)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "musolimaAt", "flt": "(?:submissive|surrender|submit|Muslim)",},
      ],
    },
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "musolimap", "flt": "(?:submissive|submit|surrender|Muslim)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "slm", "flt": "(?:greet(?!ing)|submit|pay|save)", "strTyp": "root",  "frm": "ii",  "poSp": "V", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "slm", "flt": "", "strTyp": "root",  "frm": "ii",  "poSp": "ADJ", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tasoliym", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "slm", "flt": "", "strTyp": "root",  "frm": "x", },
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sala`m", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "salam", "flt": "(?:\[the\] peace|the submission)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "salom", "flt": "(?<!\] )peace",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "silom", "flt": "Islam",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "saliym", "flt": "",},
      ],
    },
  ],
]

salah = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "", "strTyp": "root",  "frm": "ii", },
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "N", },
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "(?:standing place)",},
        { "stri": "muSal~aY", "flt": "(?:place of prayer)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "muSal~iyn", "flt": "",},
      ],
    },
  ],

      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tlw", "flt": "",},
        { "stri": "qwm", "flt": "(?:standing)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tlw", "flt": "",},
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tlw", "flt": "",},
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tlw", "flt": "",},
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "N", },
      ],
    },
  ],
      
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "tlw", "flt": "",},
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],

      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Salaw`p", "flt": "",},
        { "stri": "qay~imap", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
        { "stri": "qaA}im", "flt": "",},
      ],
    },
  ],

      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
        { "stri": "Slw", "flt": "(?:pray(?!er))",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "i",  "poSp": "V", },
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],

      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "(?:stablishment|stablishing|ncampment)", "strTyp": "root",  "frm": "iv", },
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "(?:who establish|enduring|lasting|establisher|established)", "strTyp": "root",  "frm": "iv", },
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],

      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qDy", "flt": "",},
        { "stri": "Salaw`p", "flt": "",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
        { "stri": "dlk", "flt": "",},
        { "stri": "$ms", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
        { "stri": "gsq", "flt": "",},
        { "stri": "lyl", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbH", "flt": "",},
        { "stri": "Trf", "flt": "",},
        { "stri": "nhr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
        { "stri": "Trf", "flt": "",},
        { "stri": "nhr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Slw", "flt": "",},
        { "stri": "zlf", "flt": "",},
        { "stri": "lyl", "flt": "",},
      ],
    },
  ],

        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rkE", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjd", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjd", "flt": "(?:jid|place)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjd", "flt": "^(.(?!jid|place))*$",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbH", "flt": "(?:swim|float|occup)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sbH", "flt": "(?:^((?!swim|float|occup).)*$)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kbr", "flt": "(?:magnif)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kbr", "flt": "(?:admir)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kbr", "flt": "(?:proud|arrogan)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "kbr", "flt": "(?:^((?!magnif|proud|arrogan|admir).)*$)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "hjd", "flt": " ",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qwm", "flt": "stand",},
        { "stri": "lyl", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qnt", "flt": "",},
        { "stri": "lyl", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qnt", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Any", "flt": "hour",},
        { "stri": "lyl", "flt": "",},
      ],
    },
  ],
]

mamluk_yaman = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Asr", "flt": "(?:captive|prisoner)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Asr", "flt": "(?:form)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mlk", "flt": "",},
        { "stri": "ymn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fty", "flt": "(?:boy|youth|young|servant)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fty", "flt": "girl",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Arb", "flt": "(?:use)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Arb", "flt": "(?:physical)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amw", "flt": "",},
      ],
    },
  ]
]

nisa = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mrA", "flt": "(?:woman|women|wife)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Anv", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wAd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HfZ", "flt": "",},
        { "stri": "frj", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xmr", "flt": "",},
        { "stri": "jyb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bdw", "flt": "",},
        { "stri": "zyn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "brj", "flt": "displaying",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "wDE", "flt": "",},
        { "stri": "vwb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wDE", "flt": "",},
        { "stri": "vwb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "lam", "flt": "",},
        { "stri": "HyD", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "HyD", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "qrr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "brj", "flt": "display(?!i)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "brj", "flt": "display$",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "brj", "flt": "(?:tower|constellation)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "msk", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "mwt", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "fH$", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zny", "flt": " ",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nsw", "flt": "",},
        { "stri": "Drb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fty", "flt": "girl",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "(?:married|he.*chaste)",},
        { "stri": "nkH", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "frj", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "(?:store|protect)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "qry", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "fortress",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "ing.*chaste",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "chastity",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "(?:married|he.*chaste)",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "mtE", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "wj", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nkH", "flt": "",},
        { "stri": "nsw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nkH", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bny", "flt": "[Dd]aughter",},
      ],
    },
  ],
]

ahl_kitab = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Aty", "flt": "", "strTyp": "root",  "frm": "iv",  "poSp": "V", },
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Aty", "flt": "", "strTyp": "root",  "frm": "iv", },
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "<inojiyl", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "taworaY`p", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "zbr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SHf", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sfr", "flt": "book",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "lwH", "flt": "scorching",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "lwH", "flt": "(?:[Tt]ablet|plank)",},
      ],
    },
  ],
]

badr = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "xrj", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "frq", "flt": "",},
        { "stri": "krh", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Twf", "flt": "",},
        { "stri": "$wk", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
        { "stri": "rdf", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nEs", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "g$w", "flt": "",},
        { "stri": "smw", "flt": "",},
        { "stri": "mwh", "flt": "",},
        { "stri": "vbt", "flt": "",},
        { "stri": "qdm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "frq", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wHy", "flt": "",},
        { "stri": "mlk", "flt": "",},
        { "stri": "Drb", "flt": "",},
        { "stri": "Enq", "flt": "",},
        { "stri": "bnn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Alh", "flt": "",},
        { "stri": "rmy", "flt": "",},
        { "stri": "qtl", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fAy", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "nSr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bdr", "flt": "Badr",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xrj", "flt": "",},
        { "stri": "dyr", "flt": "",},
        { "stri": "bTr", "flt": "",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$Tn", "flt": "",},
        { "stri": "nkS", "flt": "",},
        { "stri": "fAy", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rAy", "flt": "",},
        { "stri": "qll", "flt": "",},
        { "stri": "nwm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rAy", "flt": "",},
        { "stri": "qll", "flt": "",},
        { "stri": "lqy", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Edw", "flt": "",},
        { "stri": "qSw", "flt": "",},
        { "stri": "dnw", "flt": "",},
      ],
    },
  ],
]

qaynuqa = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "mrD", "flt": "",},
        { "stri": "grr", "flt": "",},
        { "stri": "dyn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ehd", "flt": "",},
        { "stri": "nqD", "flt": "",},
        { "stri": "mrr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xwn", "flt": "",},
        { "stri": "xwf", "flt": "",},
        { "stri": "nb*", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "$rd", "flt": "",},
      ],
    },
  ],
]

najran = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bhl", "flt": "",},
      ],
    },
  ],
]

uhud = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bwA", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "hmm", "flt": "",},
        { "stri": "Twf", "flt": "",},
        { "stri": "f$l", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "vlv", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "mdd", "flt": "",},
        { "stri": "xms", "flt": "",},
        { "stri": "Alf", "flt": "",},
        { "stri": "mlk", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "qTE", "flt": "",},
        { "stri": "kbt", "flt": "",},
        { "stri": "kfr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "TwE", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "rdd", "flt": "",},
        { "stri": "xsr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "f$l", "flt": "",},
        { "stri": "ESy", "flt": "",},
        { "stri": "Srf", "flt": "",},
        { "stri": "blw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SEd", "flt": "",},
        { "stri": "rsl", "flt": "",},
        { "stri": "Axr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jhl", "flt": "",},
        { "stri": "Amr", "flt": "",},
        { "stri": "naA", "flt": "",},
        { "stri": "$yA", "flt": " ",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "wly", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ywm", "flt": "",},
        { "stri": "lqy", "flt": "",},
        { "stri": "jmE", "flt": "",},
        { "stri": "Swb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Axw", "flt": "",},
        { "stri": "qEd", "flt": "",},
        { "stri": "qtl", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nEs", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "g$w", "flt": "",},
        { "stri": "Twf", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "End", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "mwt", "flt": "",},
        { "stri": "maA", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "lyn", "flt": "",},
        { "stri": "rHm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "gll", "flt": "",},
        { "stri": "nbA", "flt": "",},
        { "stri": "maA", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jwb", "flt": "",},
        { "stri": "rsl", "flt": "",},
        { "stri": "qrH", "flt": "",},
      ],
    },
  ],
]


bir_mauna = [

]


hamra = [

]

ahzab = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jnd", "flt": "",},
        { "stri": "jyA", "flt": "",},
        { "stri": "lam", "flt": "",},
        { "stri": "rAy", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "mrD", "flt": "",},
        { "stri": "wEd", "flt": "",},
        { "stri": "grr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Twf", "flt": "",},
        { "stri": "yavorib", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "qwm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "byt", "flt": "",},
        { "stri": "Ewr", "flt": "",},
        { "stri": "frr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "dxl", "flt": "",},
        { "stri": "sAl", "flt": "",},
        { "stri": "ftn", "flt": "",},
        { "stri": "Aty", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ehd", "flt": "",},
        { "stri": "laA", "flt": "",},
        { "stri": "wly", "flt": "",},
        { "stri": "dbr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ewq", "flt": "",},
        { "stri": "Axw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xwf", "flt": "",},
        { "stri": "slq", "flt": "",},
        { "stri": "lsn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hsb", "flt": "",},
        { "stri": "Hzb", "flt": "",},
        { "stri": "*hb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Amn", "flt": "",},
        { "stri": "rAy", "flt": "",},
        { "stri": "Hzb", "flt": "",},
        { "stri": "wEd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rdd", "flt": "",},
        { "stri": "kfr", "flt": "",},
        { "stri": "gyZ", "flt": "",},
      ],
    },
  ],
]

qurayza = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "SyS", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
        { "stri": "qtl", "flt": "",},
        { "stri": "Asr", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wrv", "flt": "",},
        { "stri": "ArD", "flt": "",},
        { "stri": "dwr", "flt": "",},
        { "stri": "wTA", "flt": "",},
      ],
    },
  ],
]

fidak = [

]

nadir = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "HSn", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
        { "stri": "H$r", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fyA", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "qry", "flt": "",},
        { "stri": "rsl", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfq", "flt": "",},
        { "stri": "Axw", "flt": "",},
        { "stri": "Ahl", "flt": "",},
        { "stri": "ktb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "jlw", "flt": "",},
        { "stri": "E*b", "flt": "",},
        { "stri": "dnw", "flt": "",},
      ],
    },
  ],
]

hudaybiya = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "byE", "flt": "",},
        { "stri": "$jr", "flt": "",},
      ],
    },
  ]
]

khaybar = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wEd", "flt": "",},
        { "stri": "gnm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "gnm", "flt": "",},
        { "stri": "xlf", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
]

dhu_amr = [

]

dhat_riqa = [

]

kurz = [

]

mutah = [

]

hunayn = [

]

tabuk = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "nfr", "flt": "",},
        { "stri": "vql", "flt": "",},
        { "stri": "ArD", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "bEd", "flt": "",},
        { "stri": "$qq", "flt": "",},
        { "stri": "tbE", "flt": "",},
        { "stri": "Hlf", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "krh", "flt": "",},
        { "stri": "jhd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "jhd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "A*n", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "xlf", "flt": "",},
        { "stri": "qEd", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "E*r", "flt": "",},
        { "stri": "Erb", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Aty", "flt": "",},
        { "stri": "Hml", "flt": "",},
        { "stri": "dmE", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Erb", "flt": "",},
        { "stri": "nfq", "flt": "",},
        { "stri": "grm", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rDw", "flt": "",},
        { "stri": "maEa", "flt": "",},
        { "stri": "xlf", "flt": "",},
      ],
    },
  ],
]

dirar = [
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sjd", "flt": "",},
        { "stri": "Drr", "flt": "",},
      ],
    },
  ],
]

sufyan = [

]

jhd = [
    *badr,
    *qaynuqa,
    *najran,
    *uhud,
    *bir_mauna,
    *hamra,
    *ahzab,
    *qurayza,
    *fidak,
    *nadir,
    *hudaybiya,
    *khaybar,
    *dhu_amr,
    *dhat_riqa,
    *kurz,
    *mutah,
    *hunayn,
    *tabuk,
    *dirar,
    *sufyan,
]

fadl = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fDl", "flt": "",},
        { "stri": "EalaY", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "fDl", "flt": "",},
        { "stri": "drj", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "drj", "flt": "(?:[Dd]egree|[Rr]ank)",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "drj", "flt": "",},
        { "stri": "EalaY", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "rfE", "flt": "",},
        { "stri": "drj", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "sxr", "flt": "",},
        { "stri": "bED", "flt": "",},
      ],
    },
  ],
]

zann = [
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jhl", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Amr", "flt": "",},
        { "stri": "naA", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Hrm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "tbE", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "$bh", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Slb", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "EiysaY", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "masiyH", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "nfs", "flt": "",},
        { "stri": "xyr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Amn", "flt": "",},
        { "stri": "xyr", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Afk", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "jnb", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Avm", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "",},
        { "stri": "Alh", "flt": "Allah",},
        { "stri": "swA", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Znn", "flt": "assum",},
        { "stri": "swA", "flt": "",},
      ],
    },
  ],
]

ftn = [
    [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Ehd", "flt": "",},
      ],
    },
  ],
        [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "wvq", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "blw", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "ftn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "Hml", "flt": "",},
        { "stri": "Ans", "flt": "",},
        { "stri": "Amn", "flt": "",},
      ],
    },
  ],
      [
    {
      "wrdDis": sameVrsIndicator,
      "strL": [
        { "stri": "*rr", "flt": "",},
        { "stri": "bnw", "flt": "",},
        { "stri": "A^dam", "flt": "",},
      ],
    },
  ],
]

araf = [
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "i"
                    },
                ],
                "lbl": "Erf i"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "ii"
                    },
                ],
                "lbl": "Erf ii"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "vi"
                    },
                ],
                "lbl": "Erf vi"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Erf",
                      "strTyp": "root",
                      "poSp": "V",
                      "frm": "viii"
                    },
                ],
                "lbl": "Erf viii"
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": ">aEoraAf",
                      "strTyp": "lem",
                      "poSp": "N",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "Eurof",
                      "strTyp": "lem",
                      "poSp": "N",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "maEoruwfap",
                      "strTyp": "stem",
                      "poSp": "ADJ",
                    },
                ],
            },
        ],
        [
            {
                "strL": [
                    {
                      "stri": "m~aEoruwf",
                      "strTyp": "lem",
                      "poSp": "N",
                      # "frm": "i"
                    },

                ],
            },
        ],
]

shahada = [
	*araf,
]

naSara = [
    [
      {
        "strL": [
          {
            "stri": "naSoraAniy~",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    # *nSr_isa_maryam,
    [
      {
        "strL": [
          {
            "stri": "naSiyr",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
              "stri": "masiyH",
              "strTyp": "lem",
              # "poSp": "N",
              # "frm": "i",
          },
        ],
      }
    ],
    [
      {
        "strL": [
          {
            "stri": "naSiyr",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
              "stri": "EiysaY",
              "strTyp": "lem",
              # "poSp": "N",
              # "frm": "i",
          },
        ],
      },
    ],
    [
      {
        "strL": [
          {
            "stri": "HawaAriy~uwn",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
        # "lbl": "حور iii"
      }
    ],
    # *Hwr_isa_maryam
]

hwd_yahudi = [
    *hwd,
    [
      {
        "strL": [
          {
            "stri": "yahuwdiy~",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          }
        ],
      }
    ],
]

hwd_yahudi_israel = [
    *hwd_yahudi,
    *israel,
]

kitab_munir = [
    [
      {
        "strL": [
          {
            "stri": "kita`b",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          },
          {
            "stri": "m~uniyr",
            "strTyp": "lem",
            # "poSp": "PN",
            # "frm": "i",
          }
        ],
      }
    ],
]

kutub = [
    *SHf,
    *torah,
    *injil,
    *zbr,
    *kitab_munir,
    [
      {
        "strL": [
          {
            # "stri": "kita`b",
            # "strTyp": "lem",
            "stri": "kita`bu",
            "strTyp": "stem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "muwsaY`",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "wrdDis": 2,
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
            "stri": "maA",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "wrdDis": 2,
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
            "stri": "kita`b",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "wrdDis": 2,
        "strL": [
          {
            "stri": "nzl",
            "strTyp": "root",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
            "stri": "{l~a*iY",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "qabol",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
    [
      {
        "wrdDis": 1,
        "strL": [
          {
            "stri": "maE",
            "strTyp": "lem",
            # "poSp": "V",
            # "frm": "iv",
          },
          {
            "stri": "maA",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            # "stri": "qabol",
            # "strTyp": "lem",
            # # "poSp": "N",
            # # "frm": "i",
          }
        ],
      }
    ],
]

milla_ibrahim = [
    [
      {
        "strL": [
          {
            "stri": "mil~ap",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          },
          {
            "stri": "<iboraAhiym",
            "strTyp": "lem",
            # "poSp": "N",
            # "frm": "i",
          }
        ],
      }
    ],
]

Hanif_milla_ibrahim = [
    *milla_ibrahim,
    *Hanif,
]

ahl_kitab = [
# ahl_kitab_majus_sabian = [
    *kitab_ahl,
    *majus,
    *sabian,
    *Hanif_milla_ibrahim,
    *kutub,
    *naSara,
    *hwd_yahudi_israel,
]