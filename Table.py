VersionTable = {
    "1": { 
        "version": 1,
        "moudles": 21,
        "ECC": {
            "L":{
                "databits": 152,
                "Numeric": 41, 
                "Alphanumeric": 25,
                "Byte": 17,
                "Kanji": 10
            },
            "M":{
                "databits": 128,
                "Numeric": 34, 
                "Alphanumeric": 20,
                "Byte": 14,
                "Kanji": 8
            },
            "Q":{
                "databits": 104,
                "Numeric": 27, 
                "Alphanumeric": 16,
                "Byte": 11,
                "Kanji": 7
            },
            "H":{
                "databits": 72,
                "Numeric": 17, 
                "Alphanumeric": 10,
                "Byte": 7,
                "Kanji": 4
            }
        }
    },
    "2": {
        "version": 2,
        "moudles": 25,
        "ECC": {
            "L":{
                "databits": 272,
                "Numeric": 77, 
                "Alphanumeric": 47,
                "Byte": 32,
                "Kanji": 20
            },
            "M":{
                "databits": 224,
                "Numeric": 63, 
                "Alphanumeric": 38,
                "Byte": 26,
                "Kanji": 16
            },
            "Q":{
                "databits": 176,
                "Numeric": 48, 
                "Alphanumeric": 29,
                "Byte": 20,
                "Kanji": 12
            },
            "H":{
                "databits": 128,
                "Numeric": 34, 
                "Alphanumeric": 20,
                "Byte": 14,
                "Kanji": 8
            }
        }
    },
    "3": {
        "version": 3,
        "moudles": 29,
        "ECC": {
            "L":{
                "databits": 440,
                "Numeric": 127, 
                "Alphanumeric": 77,
                "Byte": 53,
                "Kanji": 32
            },
            "M":{
                "databits": 352,
                "Numeric": 101, 
                "Alphanumeric": 61,
                "Byte": 42,
                "Kanji": 26
            },
            "Q":{
                "databits": 272,
                "Numeric": 77, 
                "Alphanumeric": 47,
                "Byte": 32,
                "Kanji": 20
            },
            "H":{
                "databits": 208,
                "Numeric": 58, 
                "Alphanumeric": 35,
                "Byte": 24,
                "Kanji": 15
            }
        }
    },
    "4": {
        "version": 4,
        "moudles": 33,
        "ECC": {
            "L":{
                "databits": 640,
                "Numeric": 187, 
                "Alphanumeric": 114,
                "Byte": 78,
                "Kanji": 48
            },
            "M":{
                "databits": 512,
                "Numeric": 149, 
                "Alphanumeric": 90,
                "Byte": 62,
                "Kanji": 38
            },
            "Q":{
                "databits": 384,
                "Numeric": 111, 
                "Alphanumeric": 67,
                "Byte": 46,
                "Kanji": 28
            },
            "H":{
                "databits": 288,
                "Numeric": 82, 
                "Alphanumeric": 50,
                "Byte": 34,
                "Kanji": 21
            }
        }
    },
    "5": {
        "version": 5,
        "moudles": 37,
        "ECC": {
            "L":{
                "databits": 864,
                "Numeric": 255, 
                "Alphanumeric": 154,
                "Byte": 106,
                "Kanji": 65
            },
            "M":{
                "databits": 688,
                "Numeric": 202, 
                "Alphanumeric": 122,
                "Byte": 84,
                "Kanji": 52
            },
            "Q":{
                "databits": 496,
                "Numeric": 144, 
                "Alphanumeric": 87,
                "Byte": 60,
                "Kanji": 37
            },
            "H":{
                "databits": 368,
                "Numeric": 106, 
                "Alphanumeric": 64,
                "Byte": 44,
                "Kanji": 27
            }
        }
    },
    "6": {
        "version": 6,
        "moudles": 41,
        "ECC": {
            "L":{
                "databits": 1088,
                "Numeric": 322, 
                "Alphanumeric": 195,
                "Byte": 134,
                "Kanji": 82
            },
            "M":{
                "databits": 864,
                "Numeric": 255, 
                "Alphanumeric": 154,
                "Byte": 106,
                "Kanji": 65
            },
            "Q":{
                "databits": 608,
                "Numeric": 178, 
                "Alphanumeric": 108,
                "Byte": 74,
                "Kanji": 45
            },
            "H":{
                "databits": 480,
                "Numeric": 139, 
                "Alphanumeric": 84,
                "Byte": 58,
                "Kanji": 36
            }
        }
    }
}


ModeIndicatorTable = {
    "Numeric": "0001",
    "Alphanumeric": "0010",
    "Byte": "0100",
    "Kanji": "1000"
}

PerBlock = {
    "1":{
        "L":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 19,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 7
        },
        "M":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 16,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 10
        },
        "Q":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 13,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 13
        },
        "H":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 9,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 17
        }
    },
    "2":{
        "L":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 34,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 10
        },
        "M":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 28,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 16
        },
        "Q":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 22,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 22
        },
        "H":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 16,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 28
        }
    },
    "3":{
        "L":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 55,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 15
        },
        "M":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 44,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 26
        },
        "Q":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 17,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 18
        },
        "H":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 13,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 22
        }
    },
    "4":{
        "L":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 80,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 20
        },
        "M":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 32,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 18
        },
        "Q":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 24,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 26
        },
        "H":{
            "num_block_g1": 4,
            "num_dc_per_block_g1": 9,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 16
        }
    },
    "5":{
        "L":{
            "num_block_g1": 1,
            "num_dc_per_block_g1": 108,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 26
        },
        "M":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 43,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 24
        },
        "Q":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 15,
            "num_block_g2": 2,
            "num_dc_per_block_g2": 16,
            "num_ecc": 18
        },
        "H":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 11,
            "num_block_g2": 2,
            "num_dc_per_block_g2": 12,
            "num_ecc": 22
        }
    },
    "6":{
        "L":{
            "num_block_g1": 2,
            "num_dc_per_block_g1": 68,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 18
        },
        "M":{
            "num_block_g1": 4,
            "num_dc_per_block_g1": 27,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 16
        },
        "Q":{
            "num_block_g1": 4,
            "num_dc_per_block_g1": 19,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 24
        },
        "H":{
            "num_block_g1": 4,
            "num_dc_per_block_g1": 15,
            "num_block_g2": 0,
            "num_dc_per_block_g2": 0,
            "num_ecc": 28
        }
    }
}