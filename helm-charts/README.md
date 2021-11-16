# Example-api helm charts

## Deploy (production) 

```markdown
helm upgrade --install --create-namespace -n example-api -f values.yaml example-api .
```

## Deploy (local)

```markdown
cp values.yaml values_local.yaml
```

Populate values such as image registry, DB credentials, ingress

```markdown
helm upgrade --install --create-namespace -n example-api-dev -f values_local.yaml example-api .
```

## Unit tests

```markdown
docker run -ti --rm -v $(pwd):/unit -w /unit jgreat/helm-unittest helm unittest --color .
```

## Lint/Validate

```markdown
docker run --rm -v $(pwd):/lint -w /unit stackrox/kube-linter lint ./
```
