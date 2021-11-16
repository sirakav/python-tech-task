{{/*
Expand the name of the chart.
*/}}
{{- define "meta.name" -}}
  {{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "meta.chart" -}}
  {{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create imagePullSecret
*/}}
{{- define "imagePullSecret" }}
{{- printf "{\"auths\": {\"%s\": {\"auth\": \"%s\"}}}" .Values.imageCredentials.registry (printf "%s:%s" .Values.imageCredentials.username .Values.imageCredentials.password | b64enc) | b64enc }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "meta.labels" -}}
app: {{ include "meta.name" $ }}
env: {{ .Values.config.ENV }}
chart: {{ include "meta.chart" $ }}
{{- end -}}

{{/*
Truncates cronjob name to 52 symbols. More info https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
*/}}
{{- define "truncateCronJobName" -}}
{{- . | replace "+" "_" | trunc 52 | trimSuffix "-" -}}
{{- end -}}

{{/*
Config checksum
*/}}
{{- define "configChecksum" -}}
{{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
{{- end -}}

{{/*
Secret checksum
*/}}
{{- define "secretChecksum" -}}
{{ include (print $.Template.BasePath "/secret.yaml") . | sha256sum }}
{{- end -}}
