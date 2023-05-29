# Get Parameters From AWS Systems Manager Parameter Store

This action is responsible for getting parameters from **AWS Systems Manager Parameter Store** and setting them in the **GITHUB_ENV** file to be used in the workflow run. So, to use this action you have to declare the following steps and also declare the **"SERVER"** environment variable:

<br>

```yaml
(...)

  env:
    SERVER: "dev" # Environment suffix (eg: "dev", "pprd", "sdx", and "prod")

  steps:

      (...)

      - name: Install Boto3
        run: pip install boto3

      - name: Split the owner and name of a repository
        uses: Add-Jazztech/github-split-repo-owner-name-action@v1.0.0

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_<ENVIRONMENT_SUFFIX>_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_<ENVIRONMENT_SUFFIX>_SECRET_KEY }}
          aws-region: us-east-1
          mask-aws-account-id: true

      - name: Action to Get Parameters From AWS SSM Parameter Store
        uses: Add-Jazztech/github-get-parameters-aws-action@v1.0.0

(...)
```

<br>

In the **"Configure AWS Credentials"** step, the values of the inputs **aws-access-key-id** and **aws-secret-access-key** need to be the values below, representing each environment:

<br>

**Development (DEV):**

<br>

- **aws-access-key-id:** ${{ secrets.AWS_DEV_ACCESS_KEY_ID }};
- **aws-secret-access-key:** ${{ secrets.AWS_DEV_ACCESS_SECRET_KEY }}.

<br>

**Pre-Production (PPRD):**

<br>

- **aws-access-key-id:** ${{ secrets.AWS_PPRD_ACCESS_KEY_ID }};
- **aws-secret-access-key:** ${{ secrets.AWS_PPRD_ACCESS_SECRET_KEY }}.

<br>

**Sandbox (SDX):**

<br>

- **aws-access-key-id:** ${{ secrets.AWS_SDX_ACCESS_KEY_ID }};
- **aws-secret-access-key:** ${{ secrets.AWS_SDX_ACCESS_SECRET_KEY }}.

<br>

**Production (PROD):**

<br>

- **aws-access-key-id:** ${{ secrets.AWS_PROD_ACCESS_KEY_ID }};
- **aws-secret-access-key:** ${{ secrets.AWS_PROD_ACCESS_SECRET_KEY }}.

<br>

These values are declared as secrets at the organization level in GitHub.
