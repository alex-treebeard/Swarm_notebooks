from viresclient import set_token
import os


if __name__ == "__main__":
    set_token(
        "https://vires.services/ows", set_default=True, token=os.getenv("TB_VIRES_TOKEN"),
    )
    # set_token(
    #     "https://staging.viresdisc.vires.services/ows", token=os.getenv("TB_VIRES_TOKEN_STAGINGDISC"),
    # )
    # set_token(
    #     "https://staging.vires.services/ows", token=os.getenv("TB_VIRES_TOKEN_STAGING"),
    # )