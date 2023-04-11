import requests

from protopy.types import Session


class AtpAgent:
    """Generic agent for interacting with any ATP app."""

    def __init__(
        self,
        service: str,
    ) -> None:
        self.service = service
        self.session: Session | None = None

    def _get_auth_header(self) -> dict[str, str]:
        """Set the access JWT in authorization header."""

        if self.session is None:
            raise Exception("Not logged in.")

        return {"Authorization": f"Bearer {self.session.accessJwt}"}

    def login(self, identifier: str, password: str) -> None:
        """Create ATP session for specified host URL."""

        res = requests.post(
            url=f"{self.service}/xrpc/com.atproto.server.createSession",
            json={"identifier": identifier, "password": password},
        )

        if res.history[0].status_code == 301:
            redirect_url = res.history[0].headers["Location"]

            res = requests.post(
                url=redirect_url,
                json={"identifier": identifier, "password": password},
            )

        self.session = Session.parse_obj(res.json())
