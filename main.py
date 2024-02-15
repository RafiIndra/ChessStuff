import torch
import torch.nn as nn
import chess
import numpy as np
import random

flippedDict = {'e4': 1,
 'd6': 2,
 'f4': 3,
 'f5': 4,
 'Nc3': 5,
 'fe4': 6,
 'Ne4': 7,
 'Nf6': 8,
 'Ng3': 9,
 'Bg4': 10,
 'Nf3': 11,
 'e6': 12,
 'Bc4': 13,
 'd5': 14,
 'Bb3': 15,
 'Bc5': 16,
 'd4': 17,
 'Bd6': 18,
 'O-O': 19,
 'Qd3': 20,
 'c6': 21,
 'c3': 22,
 'Nd7': 23,
 'Bc2': 24,
 'g6': 25,
 'h3': 26,
 'Bf5': 27,
 'Nf5': 28,
 'ef5': 29,
 'Bd2': 30,
 'Be1': 31,
 'Ne5': 32,
 'Nh5': 33,
 'Qf3': 34,
 'Qe7': 35,
 'Rc1': 36,
 'g5': 37,
 'Nd3': 38,
 'g4': 39,
 'hg4': 40,
 'fg4': 41,
 'Qd1': 42,
 'Bg3': 43,
 'Re1': 44,
 'Bf4': 45,
 'Re7': 46,
 'Bc1': 47,
 'Qg4': 48,
 'Kh8': 49,
 'Qg7': 50,
 'ed5': 51,
 'Qd5': 52,
 'Qe6': 53,
 'Be2': 54,
 'Nc6': 55,
 'Nh6': 56,
 'Bd7': 57,
 'Nb5': 58,
 'O-O-O': 59,
 'Kb8': 60,
 'Ng4': 61,
 'Qe5': 62,
 'Nc7': 63,
 'Kc7': 64,
 'Kc8': 65,
 'Be5': 66,
 'Bh5': 67,
 'Re5': 68,
 'gh5': 69,
 'Rh5': 70,
 'Rg8': 71,
 'g3': 72,
 'e5': 73,
 'de6': 74,
 'Be6': 75,
 'Rd2': 76,
 'Qc3': 77,
 'Qd2': 78,
 'Be7': 79,
 'Qf4': 80,
 'Ka8': 81,
 'Rc8': 82,
 'Rc4': 83,
 'Rh7': 84,
 'Rf4': 85,
 'Rh8': 86,
 'Bc8': 87,
 'Ne7': 88,
 'Rf8': 89,
 'Nd5': 90,
 'dc5': 91,
 'Bh3': 92,
 'gh3': 93,
 'b4': 94,
 'Qc7': 95,
 'Bh6': 96,
 'Bf8': 97,
 'Kf8': 98,
 'Bd5': 99,
 'cd5': 100,
 'Nh4': 101,
 'Re3': 102,
 'Nd2': 103,
 'Qg5': 104,
 'Rg3': 105,
 'Re8': 106,
 'Qd6': 107,
 'Kg7': 108,
 'f6': 109,
 'fe5': 110,
 'Qd4': 111,
 'Kh6': 112,
 'Re4': 113,
 'Qc1': 114,
 'Kg2': 115,
 'Qc2': 116,
 'Rh4': 117,
 'Bg2': 118,
 'e3': 119,
 'Ne2': 120,
 'de5': 121,
 'Rf1': 122,
 'Nb3': 123,
 'Bf3': 124,
 'Nd4': 125,
 'Bd4': 126,
 'Bb2': 127,
 'Qd7': 128,
 'c4': 129,
 'Qh3': 130,
 'd3': 131,
 'Na3': 132,
 'Nc2': 133,
 'dc3': 134,
 'Bc3': 135,
 'b6': 136,
 'b5': 137,
 'Qb1': 138,
 'a5': 139,
 'a4': 140,
 'c5': 141,
 'Bc7': 142,
 'Nc4': 143,
 'dc4': 144,
 'Nc8': 145,
 'Rd1': 146,
 'Nd6': 147,
 'Bf6': 148,
 'Qf6': 149,
 'Ba8': 150,
 'Qh2': 151,
 'Kf1': 152,
 'Qh1': 153,
 'Ng1': 154,
 'Bh2': 155,
 'Ke2': 156,
 'Ba1': 157,
 'Bc6': 158,
 'h6': 159,
 'Ra1': 160,
 'Re6': 161,
 'Qd8': 162,
 'Kh7': 163,
 'Ra2': 164,
 'Re2': 165,
 'Rf6': 166,
 'Be4': 167,
 'f3': 168,
 'Qg3': 169,
 'Rg2': 170,
 'Kf2': 171,
 'Qb2': 172,
 'Qa1': 173,
 'gh6': 174,
 'Bg7': 175,
 'Bf7': 176,
 'Rf7': 177,
 'Nf7': 178,
 'Kf7': 179,
 'Kg8': 180,
 'Bg5': 181,
 'ef6': 182,
 'Bb7': 183,
 'Qc8': 184,
 'Qa3': 185,
 'Ra7': 186,
 'Kh1': 187,
 'Qc5': 188,
 'Qh7': 189,
 'Qe2': 190,
 'Qg6': 191,
 'Ba6': 192,
 'Kd8': 193,
 'Qb4': 194,
 'Qa4': 195,
 'Qe8': 196,
 'Bb5': 197,
 'Qc6': 198,
 'a6': 199,
 'cd4': 200,
 'ed4': 201,
 'Qc4': 202,
 'b3': 203,
 'Bh4': 204,
 'Bb4': 205,
 'Qb5': 206,
 'Rf2': 207,
 'Nf4': 208,
 'Be3': 209,
 'Rh6': 210,
 'Qf5': 211,
 'dc6': 212,
 'Nd1': 213,
 'bc6': 214,
 'Ba4': 215,
 'Nc5': 216,
 'Rb1': 217,
 'Nb4': 218,
 'a3': 219,
 'cb5': 220,
 'Rb5': 221,
 'Rb7': 222,
 'Rd7': 223,
 'Rd8': 224,
 'Rc7': 225,
 'Na5': 226,
 'Ba7': 227,
 'Nb2': 228,
 'Ng5': 229,
 'Kh2': 230,
 'Ne6': 231,
 'Rg7': 232,
 'Ra8': 233,
 'Kg6': 234,
 'Kg3': 235,
 'Ne1': 236,
 'h4': 237,
 'h5': 238,
 'Kg5': 239,
 'Ra5': 240,
 'Bd3': 241,
 'bc3': 242,
 'Qe3': 243,
 'Qh6': 244,
 'Bb8': 245,
 'Bb1': 246,
 'Qb6': 247,
 'Kb1': 248,
 'Rg1': 249,
 'bc4': 250,
 'Rg5': 251,
 'hg5': 252,
 'hg7': 253,
 'Rh1': 254,
 'Qh8': 255,
 'Bg6': 256,
 'ed3': 257,
 'cb3': 258,
 'hg6': 259,
 'fg6': 260,
 'Qe4': 261,
 'Rb8': 262,
 'Qf7': 263,
 'Be8': 264,
 'Qf8': 265,
 'Qa5': 266,
 'd7': 267,
 'ed7': 268,
 'Ka7': 269,
 'Qa7': 270,
 'Bh7': 271,
 'ef7': 272,
 'Ke7': 273,
 'Qe1': 274,
 'Kd6': 275,
 'Kc5': 276,
 'Kb4': 277,
 'Kb6': 278,
 'Kb7': 279,
 'Qb8': 280,
 'Kc6': 281,
 'Kd5': 282,
 'Ke6': 283,
 'gf4': 284,
 'de4': 285,
 'Bb6': 286,
 'Nb6': 287,
 'Rb6': 288,
 'Kd7': 289,
 'Ke8': 290,
 'Rc6': 291,
 'Rd6': 292,
 'Qh5': 293,
 'Ng6': 294,
 'Ka6': 295,
 'fe6': 296,
 'cb7': 297,
 'Qb3': 298,
 'ba5': 299,
 'Qb7': 300,
 'Ba5': 301,
 'Nh3': 302,
 'Ng7': 303,
 'ab6': 304,
 'Rb3': 305,
 'Rd4': 306,
 'Rh3': 307,
 'Qh4': 308,
 'gh4': 309,
 'Nf2': 310,
 'Qg1': 311,
 'Qa2': 312,
 'ed6': 313,
 'cd6': 314,
 'Kf4': 315,
 'Kf5': 316,
 'Kf6': 317,
 'Nf8': 318,
 'Bg8': 319,
 'Rh2': 320,
 'ab5': 321,
 'Ra4': 322,
 'Kb2': 323,
 'Kc3': 324,
 'Ra6': 325,
 'Ka5': 326,
 'ab4': 327,
 'Kb3': 328,
 'Ka2': 329,
 'Kd2': 330,
 'gf6': 331,
 'cd3': 332,
 'Rd3': 333,
 'Rb2': 334,
 'ef3': 335,
 'Rf3': 336,
 'Na4': 337,
 'Bf1': 338,
 'cb4': 339,
 'Qa6': 340,
 'Kg1': 341,
 'Nd8': 342,
 'Qf2': 343,
 'Nh2': 344,
 'g2': 345,
 'h2': 346,
 'Bf2': 347,
 'Qg8': 348,
 'Qa8': 349,
 'Bd1': 350,
 'ba4': 351,
 'ba3': 352,
 'Bd8': 353,
 'Rf5': 354,
 'Kb5': 355,
 'Kc4': 356,
 'Qf1': 357,
 'ef4': 358,
 'Kc2': 359,
 'Ne3': 360,
 'Ng2': 361,
 'Kh5': 362,
 'Kg4': 363,
 'Rd5': 364,
 'Kf3': 365,
 'Kd1': 366,
 'Rg4': 367,
 'Ke3': 368,
 'Ke1': 369,
 'Nh8': 370,
 'fe3': 371,
 'Kh4': 372,
 'Kh3': 373,
 'gf3': 374,
 'Nb8': 375,
 'Na6': 376,
 'Nc1': 377,
 'Nf1': 378,
 'Ng8': 379,
 'Na8': 380,
 'e7': 381,
 'ef8': 382,
 'Qg2': 383,
 'Na2': 384,
 'ba6': 385,
 'fg3': 386,
 'h7': 387,
 'h8': 388,
 'Rg6': 389,
 'Ba2': 390,
 'bc5': 391,
 'c7': 392,
 'c8': 393,
 'd8': 394,
 'gf5': 395,
 'Rb4': 396,
 'Rc5': 397,
 'hg3': 398,
 'a7': 399,
 'ab8': 400,
 'Na7': 401,
 'e8': 402,
 'Ba3': 403,
 'cb2': 404,
 'Bh1': 405,
 'Bg1': 406,
 'ab3': 407,
 'Rc3': 408,
 'Kd3': 409,
 'Kd4': 410,
 'g8': 411,
 'ab7': 412,
 'Nh7': 413,
 'Kc1': 414,
 'fg8': 415,
 'Nb7': 416,
 'fg7': 417,
 'gf7': 418,
 'Nh1': 419,
 'Nb1': 420,
 'Ne8': 421,
 'Ke5': 422,
 'Rc2': 423,
 'fg2': 424,
 'gf1': 425,
 'Bh8': 426,
 'Ka4': 427,
 'd2': 428,
 'de3': 429,
 'fg5': 430,
 'Ra3': 431,
 'a8': 432,
 'gf2': 433,
 'de7': 434,
 'a2': 435,
 'g7': 436,
 'b2': 437,
 'b1': 438,
 'fe7': 439,
 'cb6': 440,
 'bc2': 441,
 'f7': 442,
 'f8': 443,
 'cd7': 444,
 'ba2': 445,
 'hg2': 446,
 'Ka3': 447,
 'Ka1': 448,
 'cd8': 449,
 'b7': 450,
 'b8': 451,
 'gh2': 452,
 'c2': 453,
 'Ke4': 454,
 'Na1': 455,
 'e2': 456,
 'ef1': 457,
 'ef2': 458,
 'de8': 459,
 'dc7': 460,
 'f2': 461,
 'ba7': 462,
 'c1': 463,
 'ba8': 464,
 'e1': 465,
 'ab2': 466,
 'gh7': 467,
 'd1': 468,
 'de2': 469,
 'f1': 470,
 'a1': 471,
 'cb8': 472,
 'cd2': 473,
 'gh8': 474,
 'ed8': 475,
 'bc7': 476,
 'fe8': 477,
 'dc8': 478,
 'fe2': 479,
 'hg8': 480,
 'bc8': 481,
 'fg1': 482,
 'dc2': 483,
 'gf8': 484,
 'h1': 485,
 'ba1': 486,
 'ed2': 487,
 'ab1': 488,
 'g1': 489,
 'de1': 490,
 'gh1': 491,
 'dc1': 492,
 'cd1': 493,
 'bc1': 494,
 'cb1': 495,
 'hg1': 496,
 'fe1': 497,
 'ed1': 498}
dictionary = {1: 'e4',
 2: 'd6',
 3: 'f4',
 4: 'f5',
 5: 'Nc3',
 6: 'fe4',
 7: 'Ne4',
 8: 'Nf6',
 9: 'Ng3',
 10: 'Bg4',
 11: 'Nf3',
 12: 'e6',
 13: 'Bc4',
 14: 'd5',
 15: 'Bb3',
 16: 'Bc5',
 17: 'd4',
 18: 'Bd6',
 19: 'O-O',
 20: 'Qd3',
 21: 'c6',
 22: 'c3',
 23: 'Nd7',
 24: 'Bc2',
 25: 'g6',
 26: 'h3',
 27: 'Bf5',
 28: 'Nf5',
 29: 'ef5',
 30: 'Bd2',
 31: 'Be1',
 32: 'Ne5',
 33: 'Nh5',
 34: 'Qf3',
 35: 'Qe7',
 36: 'Rc1',
 37: 'g5',
 38: 'Nd3',
 39: 'g4',
 40: 'hg4',
 41: 'fg4',
 42: 'Qd1',
 43: 'Bg3',
 44: 'Re1',
 45: 'Bf4',
 46: 'Re7',
 47: 'Bc1',
 48: 'Qg4',
 49: 'Kh8',
 50: 'Qg7',
 51: 'ed5',
 52: 'Qd5',
 53: 'Qe6',
 54: 'Be2',
 55: 'Nc6',
 56: 'Nh6',
 57: 'Bd7',
 58: 'Nb5',
 59: 'O-O-O',
 60: 'Kb8',
 61: 'Ng4',
 62: 'Qe5',
 63: 'Nc7',
 64: 'Kc7',
 65: 'Kc8',
 66: 'Be5',
 67: 'Bh5',
 68: 'Re5',
 69: 'gh5',
 70: 'Rh5',
 71: 'Rg8',
 72: 'g3',
 73: 'e5',
 74: 'de6',
 75: 'Be6',
 76: 'Rd2',
 77: 'Qc3',
 78: 'Qd2',
 79: 'Be7',
 80: 'Qf4',
 81: 'Ka8',
 82: 'Rc8',
 83: 'Rc4',
 84: 'Rh7',
 85: 'Rf4',
 86: 'Rh8',
 87: 'Bc8',
 88: 'Ne7',
 89: 'Rf8',
 90: 'Nd5',
 91: 'dc5',
 92: 'Bh3',
 93: 'gh3',
 94: 'b4',
 95: 'Qc7',
 96: 'Bh6',
 97: 'Bf8',
 98: 'Kf8',
 99: 'Bd5',
 100: 'cd5',
 101: 'Nh4',
 102: 'Re3',
 103: 'Nd2',
 104: 'Qg5',
 105: 'Rg3',
 106: 'Re8',
 107: 'Qd6',
 108: 'Kg7',
 109: 'f6',
 110: 'fe5',
 111: 'Qd4',
 112: 'Kh6',
 113: 'Re4',
 114: 'Qc1',
 115: 'Kg2',
 116: 'Qc2',
 117: 'Rh4',
 118: 'Bg2',
 119: 'e3',
 120: 'Ne2',
 121: 'de5',
 122: 'Rf1',
 123: 'Nb3',
 124: 'Bf3',
 125: 'Nd4',
 126: 'Bd4',
 127: 'Bb2',
 128: 'Qd7',
 129: 'c4',
 130: 'Qh3',
 131: 'd3',
 132: 'Na3',
 133: 'Nc2',
 134: 'dc3',
 135: 'Bc3',
 136: 'b6',
 137: 'b5',
 138: 'Qb1',
 139: 'a5',
 140: 'a4',
 141: 'c5',
 142: 'Bc7',
 143: 'Nc4',
 144: 'dc4',
 145: 'Nc8',
 146: 'Rd1',
 147: 'Nd6',
 148: 'Bf6',
 149: 'Qf6',
 150: 'Ba8',
 151: 'Qh2',
 152: 'Kf1',
 153: 'Qh1',
 154: 'Ng1',
 155: 'Bh2',
 156: 'Ke2',
 157: 'Ba1',
 158: 'Bc6',
 159: 'h6',
 160: 'Ra1',
 161: 'Re6',
 162: 'Qd8',
 163: 'Kh7',
 164: 'Ra2',
 165: 'Re2',
 166: 'Rf6',
 167: 'Be4',
 168: 'f3',
 169: 'Qg3',
 170: 'Rg2',
 171: 'Kf2',
 172: 'Qb2',
 173: 'Qa1',
 174: 'gh6',
 175: 'Bg7',
 176: 'Bf7',
 177: 'Rf7',
 178: 'Nf7',
 179: 'Kf7',
 180: 'Kg8',
 181: 'Bg5',
 182: 'ef6',
 183: 'Bb7',
 184: 'Qc8',
 185: 'Qa3',
 186: 'Ra7',
 187: 'Kh1',
 188: 'Qc5',
 189: 'Qh7',
 190: 'Qe2',
 191: 'Qg6',
 192: 'Ba6',
 193: 'Kd8',
 194: 'Qb4',
 195: 'Qa4',
 196: 'Qe8',
 197: 'Bb5',
 198: 'Qc6',
 199: 'a6',
 200: 'cd4',
 201: 'ed4',
 202: 'Qc4',
 203: 'b3',
 204: 'Bh4',
 205: 'Bb4',
 206: 'Qb5',
 207: 'Rf2',
 208: 'Nf4',
 209: 'Be3',
 210: 'Rh6',
 211: 'Qf5',
 212: 'dc6',
 213: 'Nd1',
 214: 'bc6',
 215: 'Ba4',
 216: 'Nc5',
 217: 'Rb1',
 218: 'Nb4',
 219: 'a3',
 220: 'cb5',
 221: 'Rb5',
 222: 'Rb7',
 223: 'Rd7',
 224: 'Rd8',
 225: 'Rc7',
 226: 'Na5',
 227: 'Ba7',
 228: 'Nb2',
 229: 'Ng5',
 230: 'Kh2',
 231: 'Ne6',
 232: 'Rg7',
 233: 'Ra8',
 234: 'Kg6',
 235: 'Kg3',
 236: 'Ne1',
 237: 'h4',
 238: 'h5',
 239: 'Kg5',
 240: 'Ra5',
 241: 'Bd3',
 242: 'bc3',
 243: 'Qe3',
 244: 'Qh6',
 245: 'Bb8',
 246: 'Bb1',
 247: 'Qb6',
 248: 'Kb1',
 249: 'Rg1',
 250: 'bc4',
 251: 'Rg5',
 252: 'hg5',
 253: 'hg7',
 254: 'Rh1',
 255: 'Qh8',
 256: 'Bg6',
 257: 'ed3',
 258: 'cb3',
 259: 'hg6',
 260: 'fg6',
 261: 'Qe4',
 262: 'Rb8',
 263: 'Qf7',
 264: 'Be8',
 265: 'Qf8',
 266: 'Qa5',
 267: 'd7',
 268: 'ed7',
 269: 'Ka7',
 270: 'Qa7',
 271: 'Bh7',
 272: 'ef7',
 273: 'Ke7',
 274: 'Qe1',
 275: 'Kd6',
 276: 'Kc5',
 277: 'Kb4',
 278: 'Kb6',
 279: 'Kb7',
 280: 'Qb8',
 281: 'Kc6',
 282: 'Kd5',
 283: 'Ke6',
 284: 'gf4',
 285: 'de4',
 286: 'Bb6',
 287: 'Nb6',
 288: 'Rb6',
 289: 'Kd7',
 290: 'Ke8',
 291: 'Rc6',
 292: 'Rd6',
 293: 'Qh5',
 294: 'Ng6',
 295: 'Ka6',
 296: 'fe6',
 297: 'cb7',
 298: 'Qb3',
 299: 'ba5',
 300: 'Qb7',
 301: 'Ba5',
 302: 'Nh3',
 303: 'Ng7',
 304: 'ab6',
 305: 'Rb3',
 306: 'Rd4',
 307: 'Rh3',
 308: 'Qh4',
 309: 'gh4',
 310: 'Nf2',
 311: 'Qg1',
 312: 'Qa2',
 313: 'ed6',
 314: 'cd6',
 315: 'Kf4',
 316: 'Kf5',
 317: 'Kf6',
 318: 'Nf8',
 319: 'Bg8',
 320: 'Rh2',
 321: 'ab5',
 322: 'Ra4',
 323: 'Kb2',
 324: 'Kc3',
 325: 'Ra6',
 326: 'Ka5',
 327: 'ab4',
 328: 'Kb3',
 329: 'Ka2',
 330: 'Kd2',
 331: 'gf6',
 332: 'cd3',
 333: 'Rd3',
 334: 'Rb2',
 335: 'ef3',
 336: 'Rf3',
 337: 'Na4',
 338: 'Bf1',
 339: 'cb4',
 340: 'Qa6',
 341: 'Kg1',
 342: 'Nd8',
 343: 'Qf2',
 344: 'Nh2',
 345: 'g2',
 346: 'h2',
 347: 'Bf2',
 348: 'Qg8',
 349: 'Qa8',
 350: 'Bd1',
 351: 'ba4',
 352: 'ba3',
 353: 'Bd8',
 354: 'Rf5',
 355: 'Kb5',
 356: 'Kc4',
 357: 'Qf1',
 358: 'ef4',
 359: 'Kc2',
 360: 'Ne3',
 361: 'Ng2',
 362: 'Kh5',
 363: 'Kg4',
 364: 'Rd5',
 365: 'Kf3',
 366: 'Kd1',
 367: 'Rg4',
 368: 'Ke3',
 369: 'Ke1',
 370: 'Nh8',
 371: 'fe3',
 372: 'Kh4',
 373: 'Kh3',
 374: 'gf3',
 375: 'Nb8',
 376: 'Na6',
 377: 'Nc1',
 378: 'Nf1',
 379: 'Ng8',
 380: 'Na8',
 381: 'e7',
 382: 'ef8',
 383: 'Qg2',
 384: 'Na2',
 385: 'ba6',
 386: 'fg3',
 387: 'h7',
 388: 'h8',
 389: 'Rg6',
 390: 'Ba2',
 391: 'bc5',
 392: 'c7',
 393: 'c8',
 394: 'd8',
 395: 'gf5',
 396: 'Rb4',
 397: 'Rc5',
 398: 'hg3',
 399: 'a7',
 400: 'ab8',
 401: 'Na7',
 402: 'e8',
 403: 'Ba3',
 404: 'cb2',
 405: 'Bh1',
 406: 'Bg1',
 407: 'ab3',
 408: 'Rc3',
 409: 'Kd3',
 410: 'Kd4',
 411: 'g8',
 412: 'ab7',
 413: 'Nh7',
 414: 'Kc1',
 415: 'fg8',
 416: 'Nb7',
 417: 'fg7',
 418: 'gf7',
 419: 'Nh1',
 420: 'Nb1',
 421: 'Ne8',
 422: 'Ke5',
 423: 'Rc2',
 424: 'fg2',
 425: 'gf1',
 426: 'Bh8',
 427: 'Ka4',
 428: 'd2',
 429: 'de3',
 430: 'fg5',
 431: 'Ra3',
 432: 'a8',
 433: 'gf2',
 434: 'de7',
 435: 'a2',
 436: 'g7',
 437: 'b2',
 438: 'b1',
 439: 'fe7',
 440: 'cb6',
 441: 'bc2',
 442: 'f7',
 443: 'f8',
 444: 'cd7',
 445: 'ba2',
 446: 'hg2',
 447: 'Ka3',
 448: 'Ka1',
 449: 'cd8',
 450: 'b7',
 451: 'b8',
 452: 'gh2',
 453: 'c2',
 454: 'Ke4',
 455: 'Na1',
 456: 'e2',
 457: 'ef1',
 458: 'ef2',
 459: 'de8',
 460: 'dc7',
 461: 'f2',
 462: 'ba7',
 463: 'c1',
 464: 'ba8',
 465: 'e1',
 466: 'ab2',
 467: 'gh7',
 468: 'd1',
 469: 'de2',
 470: 'f1',
 471: 'a1',
 472: 'cb8',
 473: 'cd2',
 474: 'gh8',
 475: 'ed8',
 476: 'bc7',
 477: 'fe8',
 478: 'dc8',
 479: 'fe2',
 480: 'hg8',
 481: 'bc8',
 482: 'fg1',
 483: 'dc2',
 484: 'gf8',
 485: 'h1',
 486: 'ba1',
 487: 'ed2',
 488: 'ab1',
 489: 'g1',
 490: 'de1',
 491: 'gh1',
 492: 'dc1',
 493: 'cd1',
 494: 'bc1',
 495: 'cb1',
 496: 'hg1',
 497: 'fe1',
 498: 'ed1'}


hidden_size = 64; num_classes = 499
embed_dim = 32
input_size = 98
num_layers = 1

class myLSTM(nn.Module):
 def __init__(self, input_size, hidden_size, num_layers, num_classes):
  super(myLSTM, self).__init__()
  self.num_layers = num_layers
  self.hidden_size = hidden_size
  self.embed_dim = embed_dim
  self.embed = nn.Embedding(num_classes, embed_dim)
  self.lstm = nn.LSTM(embed_dim, hidden_size, num_layers, batch_first=True)
  self.fc = nn.Linear(hidden_size, num_classes)

 def forward(self, x):
  h0 = torch.zeros(self.num_layers,
                   x.shape[1],
                   self.hidden_size)
  c0 = torch.zeros(self.num_layers,
                   x.shape[1],
                   self.hidden_size)

  embed = self.embed(x.long())
  out, _ = self.lstm(embed[0].float(), (h0, c0))
  out2 = out[:, -1, :]
  out5 = self.fc(out2)
  return out5

model2 = myLSTM(input_size, hidden_size, num_layers, num_classes)
model2.load_state_dict(torch.load('ingite.pt'))
model2.eval()

def encode(games):
  print(f'input: {games}')
  game = games
  for j, move in enumerate(game):
   temp = move.replace("x", "")
   temp = temp.replace("+", "")
   temp = temp.replace("#", "")
   temp = temp.replace("0!", "")
   temp = temp.replace("!", "")
   temp = temp.replace("00", "")
   temp = temp.replace("=R", "")
   temp = temp.replace("=Q", "")
   temp = temp.replace("=N", "")
   temp = temp.replace("=B", "")
   if (len(temp) > 3) and (temp[0] != "O"):
    temp = temp[0] + temp[-2] + temp[-1]
   try:
    game[j] = flippedDict[temp]
   except KeyError:
    game[j] = 0
  print(game)
  for j in range(98 - len(game)):
    game.insert(0, 0)
  return game

def is_promotion(move):
 if move.islower() and (move[-1] == "1" or move[-1] == "8"):
  return True
 else:
  return False

def is_ambiguous(move):
 piece = {"N": 2, "B": 3, "R": 4, "Q": 5}
 try:
  board.parse_san(move)
 except chess.AmbiguousMoveError:
  return (True, piece[move[0]])
 except chess.IllegalMoveError:
  return False
 else:
  return False

def is_illegal(move):
 try:
  board.parse_san(move)
 except chess.IllegalMoveError:
  if is_promotion(move):
   return False
  else:
   return True
 except chess.AmbiguousMoveError:
  return False

def is_illegalAbs(move):
 try:
  board.parse_san(move)
  # print(f"{move} is illegal")
 except:
  return True

board = chess.Board()
while True:
  msg = input()
  if msg == "uci":
    print("uciok")

  elif msg == "isready":
    print("readyok")

  elif msg==("ucinewgame"):
   continue

  elif msg.startswith("position startpos"):
    board.reset()
    if len(msg.split()) <=3:
      choice = ["e4", "d4"]
      move = choice[random.randint(0,1)]
      continue
    moves = msg.split(" ")[3:]
    moves2 = []
    for move in moves:
      moves2.append(board.san(board.parse_san(move)))
      board.push_san(move)
    # print(f'woi {moves2}')
    data = encode(moves2)
    data = torch.tensor([[data]])
    print(data)
    nextMove = model2(data)
    sorted = np.argsort(nextMove[0].detach().numpy())[::-1]
    prediksi = np.argmax(nextMove.detach())
    move = dictionary[prediksi.item()]
    print(move)
    max = float("-inf")

    try:
     board.parse_san(move)

    except chess.AmbiguousMoveError:
     squares = board.pieces(is_ambiguous(move)[1], 1)
     for square in squares:
      try:
       board.find_move(square, chess.parse_square(move[-2:]))
       move = (move[0] + chess.square_name(square) + move[-2:])
      except:
       pass

    except chess.IllegalMoveError:
     # move is undefined promotion
     for index in sorted:
      if index == 0:
       continue
      if is_illegal(dictionary[index]):
       continue

      if is_ambiguous(dictionary[index]):
       squares = board.pieces(is_ambiguous(dictionary[index])[1], 1)
       for square in squares:
        try:
         board.find_move(square, chess.parse_square(dictionary[index][-2:]))
         move = (dictionary[index][0] + chess.square_name(square) + dictionary[index][-2:])
        except:
         pass
       break

      if is_promotion(dictionary[index]):
       moveTemp = dictionary[index] + "=Q"
       if is_illegalAbs(moveTemp):
        continue
       move = moveTemp
       break

      else:
       move = dictionary[index]
       break

  elif msg.startswith("go"):
   print(f"bestmove {board.push_san(move)}")
   # if specialCase:
    # print(f'bestmove {board.push_san(moveFinal)}')
   # else:
    # print(f"bestmove {board.push_san(str(dictionary[maxIndex]))}")
  elif msg  == "quit":
    break