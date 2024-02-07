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

PerBlockTable = {
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







############################################################################################

NormalLocationPoint = [(0, 0, 1), (0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), 
(0, 5, 1), (0, 6, 1), (1, 0, 1), (1, 1, 0), (1, 2, 0), 
(1, 3, 0), (1, 4, 0), (1, 5, 0), (1, 6, 1), (2, 0, 1), 
(2, 1, 0), (2, 2, 1), (2, 3, 1), (2, 4, 1), (2, 5, 0), 
(2, 6, 1), (3, 0, 1), (3, 1, 0), (3, 2, 1), (3, 3, 1), 
(3, 4, 1), (3, 5, 0), (3, 6, 1), (4, 0, 1), (4, 1, 0), 
(4, 2, 1), (4, 3, 1), (4, 4, 1), (4, 5, 0), (4, 6, 1), 
(5, 0, 1), (5, 1, 0), (5, 2, 0), (5, 3, 0), (5, 4, 0), 
(5, 5, 0), (5, 6, 1), (6, 0, 1), (6, 1, 1), (6, 2, 1), 
(6, 3, 1), (6, 4, 1), (6, 5, 1), (6, 6, 1)]

############################################################################################


############################################################################################
AlignmentPatternTable = {
    "1":[],
    "2":[6, 18],
    "3":[6, 22],
    "4":[6, 26],
    "5":[6, 30],
    "6":[6, 34],
    "7":[6, 22, 38],
    "8":[6, 24, 42],
    "9":[6, 26, 46],
    "10":[6, 28, 50]
}



############################################################################################

############################################################################################
ECCFomatTable = {
    '01000': '111011111000100', 
    '01001': '111001011110011', 
    '01010': '111110110101010', 
    '01011': '111100010011101', 
    '01100': '110011000101111', 
    '01101': '110001100011000', 
    '01110': '110110001000001', 
    '01111': '110100101110110', 
    '00000': '101010000010010', 
    '00001': '101000100100101', 
    '00010': '101111001111100', 
    '00011': '101101101001011', 
    '00100': '100010111111001', 
    '00101': '100000011001110', 
    '00110': '100111110010111', 
    '00111': '100101010100000', 
    '11000': '011010101011111', 
    '11001': '011000001101000', 
    '11010': '011111100110001', 
    '11011': '011101000000110', 
    '11100': '010010010110100', 
    '11101': '010000110000011', 
    '11110': '010111011011010', 
    '11111': '010101111101101', 
    '10000': '001011010001001', 
    '10001': '001001110111110', 
    '10010': '001110011100111', 
    '10011': '001100111010000', 
    '10100': '000011101100010', 
    '10101': '000001001010101', 
    '10110': '000110100001100', 
    '10111': '000100000111011'
}

def ECCFomatSiteTable(version: int):
    length = version * 4 + 17
    Table = {
        "8,0": 0,
        "8,1": 1,
        "8,2": 2,
        "8,3": 3,
        "8,4": 4,
        "8,5": 5,
        "8,7": 6,
        "8,8": 7,
        "7,8": 8,
        "5,8": 9,
        "4,8": 10,
        "3,8": 11,
        "2,8": 12,
        "1,8": 13,
        "0,8": 14,
        str(length - 1) + ",8": 0,
        str(length - 2) + ",8": 1,
        str(length - 3) + ",8": 2,
        str(length - 4) + ",8": 3,
        str(length - 5) + ",8": 4,
        str(length - 6) + ",8": 5,
        str(length - 7) + ",8": 6,
        "8," + str(length - 8): 7,
        "8," + str(length - 7): 8,
        "8," + str(length - 6): 9,
        "8," + str(length - 5): 10,
        "8," + str(length - 4): 11,
        "8," + str(length - 3): 12,
        "8," + str(length - 2): 13,
        "8," + str(length - 1): 14
    }
    return Table
############################################################################################
