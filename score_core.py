"""Minimal public core of the Aigaane Truth Engine."""

WEIGHTS = {
    "EMPIRICAL_PHYSICAL": (0.25, 0.45, 0.30),
    "HERMENEUTIC_DHARMA": (0.60, 0.15, 0.25),
    "FORMAL_LOGICAL": (0.20, 0.60, 0.20),
}


def bayes_posterior(prior, p_e_h, p_e_not_h):
    lr = p_e_h / p_e_not_h if p_e_not_h else float("inf")
    numer = p_e_h * prior
    denom = numer + p_e_not_h * (1.0 - prior)
    return lr, numer / denom if denom else prior


def apply_upadhi_tarka(p_e_not_h, U=0.0, T=0.0):
    # Do not stack U if it is already inside p_e_not_h.
    p = (p_e_not_h + (1.0 - p_e_not_h) * U) * (1.0 - T)
    return min(1.0, max(1e-12, p))


def T_C(s1, s2, s3, F, profile="EMPIRICAL_PHYSICAL"):
    w1, w2, w3 = WEIGHTS[profile]
    return round((w1 * s1 + w2 * s2 + w3 * s3) * (1.0 - F), 4)


if __name__ == "__main__":
    lr, post = bayes_posterior(0.15, 0.80, 0.85)
    print("physics LR", round(lr, 4), "S2", round(post, 4))
    print("physics T", T_C(0.25, 0.1424, 0.25, 0.76, "EMPIRICAL_PHYSICAL"))
    lr2, post2 = bayes_posterior(0.70, 0.90, 0.20)
    print("lore LR", round(lr2, 4), "S2", round(post2, 4))
    print("lore T", T_C(0.90, post2, 0.90, 0.05, "HERMENEUTIC_DHARMA"))
