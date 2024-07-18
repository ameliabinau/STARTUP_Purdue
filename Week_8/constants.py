charged_long_lived_abs_pids = (
    11,  # e
    13,  # mu
    211,  # pi
    321,  # K+
    2212,  # p
    3112,  # Sigma-
    3222,  # Sigma+
    3312,  # Xi-
    3334,  # Omega-
)

long_lived_abs_pids = (
    11,  # e
    12,  # nu_e
    13,  # mu
    14,  # nu_mu
    16,  # nu_tau
    22,  # gamma
    130,  # KL
    211,  # pi
    310,  # KS
    321,  # K+
    2112,  # n
    2212,  # p
    3112,  # Sigma-
    3122,  # Lambda
    3222,  # Sigma+
    3312,  # Xi-
    3322,  # Xi0
    3334,  # Omega-
)

long_lived_pids = (
    11,  # e
    -11,
    12,  # nu_e
    -12,
    13,  # mu
    -13,
    14,  # nu_mu
    -14,
    16,  # nu_tau
    -16,
    22,  # gamma
    130,  # KL
    211,  # pi
    -211,
    310,  # KS
    321,  # K+
    -321,
    2112,  # n
    -2112,
    2212,  # p
    -2212,
    3112,  # Sigma-
    -3112,
    3122,  # Lambda
    -3122,
    3222,  # Sigma+
    -3222,
    3312,  # Xi-
    -3312,
    3322,  # Xi0
    -3322,
    3334,  # Omega-
    -3334,
)

final_state_mask = 1 << 0
association_chain_mask = 1 << 1
track_associated_mask = 1 << 2
long_lived_mask = 1 << 3
prompt_mask = 1 << 4
prompt_long_lived_mask = long_lived_mask | prompt_mask
