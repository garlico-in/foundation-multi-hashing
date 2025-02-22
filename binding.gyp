{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                'algorithms/allium.c',
                "algorithms/bcrypt.c",
                "algorithms/blake.c",
                "algorithms/blake2s.c",
                "algorithms/c11.c",
                "algorithms/fresh.c",
                "algorithms/fugue.c",
                "algorithms/gost.c",
                "algorithms/gr.c",
                "algorithms/groestl.c",
                "algorithms/hefty1.c",
                "algorithms/keccak.c",
                "algorithms/lbry.c",
                "algorithms/minotaur.c",
                "algorithms/nist5.c",
                "algorithms/phi1612.c",
                "algorithms/quark.c",
                "algorithms/qubit.c",
                "algorithms/scryptn.c",
                "algorithms/sha256d.c",
                "algorithms/shavite3.c",
                "algorithms/skein.c",
                "algorithms/sm3.c",
                "algorithms/tribus.c",
                "algorithms/verthash.c",
                "algorithms/whirlpoolx.c",
                "algorithms/x11.c",
                "algorithms/x13.c",
                "algorithms/x15.c",
                "algorithms/x16r.c",
                "algorithms/x16rt.c",
                "algorithms/sha3/aes_helper.c",
                "algorithms/sha3/hamsi.c",
                "algorithms/sha3/KeccakP-800-reference.c",
                "algorithms/sha3/sha3.c",
                "algorithms/sha3/sph_haval.c",
                "algorithms/sha3/sph_hefty1.c",
                "algorithms/sha3/sph_fugue.c",
                "algorithms/sha3/sph_blake.c",
                "algorithms/sha3/sph_blake2s.c",
                "algorithms/sha3/sph_bmw.c",
                "algorithms/sha3/sph_cubehash.c",
                "algorithms/sha3/sph_echo.c",
                "algorithms/sha3/sph_gost.c",
                "algorithms/sha3/sph_groestl.c",
                "algorithms/sha3/sph_jh.c",
                "algorithms/sha3/sph_keccak.c",
                "algorithms/sha3/sph_luffa.c",
                "algorithms/sha3/sph_shavite.c",
                "algorithms/sha3/sph_simd.c",
                "algorithms/sha3/sph_skein.c",
                "algorithms/sha3/sph_whirlpool.c",
                "algorithms/sha3/sph_shabal.c",
                "algorithms/sha3/sph_ripemd.c",
                "algorithms/sha3/sph_sha2.c",
                "algorithms/sha3/sph_sha2big.c",
                "algorithms/sha3/sph_tiger.c",
                "algorithms/allium/lyra2.c",
                'algorithms/cryptonote/cryptonight_dark_lite.c',
                'algorithms/cryptonote/cryptonight_dark.c',
                'algorithms/cryptonote/cryptonight_fast.c',
                'algorithms/cryptonote/cryptonight_lite.c',
                'algorithms/cryptonote/cryptonight_soft_shell.c',
                'algorithms/cryptonote/cryptonight_turtle_lite.c',
                'algorithms/cryptonote/cryptonight_turtle.c',
                'algorithms/cryptonote/cryptonight.c',
                'algorithms/crypto/aesb.c',
                'algorithms/crypto/c_blake256.c',
                'algorithms/crypto/c_groestl.c',
                'algorithms/crypto/c_jh.c',
                'algorithms/crypto/c_keccak.c',
                'algorithms/crypto/c_skein.c',
                'algorithms/crypto/hash.c',
                'algorithms/crypto/oaes_lib.c',
                'algorithms/crypto/wild_keccak.cpp',
                'algorithms/yespower/yespower.c',
                'algorithms/yespower/crypto/sha256.c'
            ],
            'conditions': [],
            "include_dirs": [],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
