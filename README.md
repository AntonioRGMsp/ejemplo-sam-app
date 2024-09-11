# ejemplo-tony-sam-app

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- tony_save_json_on_mongo_db - Code for upload json data to MongoDB.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code.
- template.yaml - A template that defines the application's AWS resources.

### Pasos para el Deploy

1. Entra la terminal PowerShell y dirigete hacia el directorio donde tienes la aplicación SAM. Ejemplo:

```bash
C:\Users\${user}\Documents\repositories\ejemplo-tony-sam-app
```

2. Asegurate de que tu archivo `template.yaml` sea correcto, ejecutándo el siguiente comando:

```bash
sam validate
```

3. Si tu archivo `template.yaml` está validado, construye la carpeta de producción de esta aplicación (Build), ejecutando el siguiente comando.

```bash
sam build
```

4. Ahora despliega la aplicación. Ejecuta el siguiente comando:

```bash
sam deploy --profile default --guided --capabilities CAPABILITY_NAMED_IAM --config-env test
```

Después de ejecutar el comando completa los siguientes prompts:

- **Stack Name**: Nombre del Stack que vas a desplegar en CloudFormation. El nombre debe ser ÚNICO en tu cuenta y región de AWS. Ejemplo: `ejemplo-tony-sam-app`.

- **AWS Region**: Selecciona la región donde vas a desplegar la aplicación. Por ejemplo: `us-east-1`

- **Confirm changes before deploy**: Selecciona YES si deseas hacer una revisión manual antes de hacer deploy. Selecciona NO si quieres que el deploy se haga automáticamente una vez aplicados tus cambios en el template.

- **Allow SAM CLI IAM role creation**: YES para permitir que SAM CLI pueda crear roles y recursos de IAM. NO para negar esos permisos.

Muchas plantillas de AWS SAM, incluido este ejemplo, crean roles de AWS IAM necesarios para las funciones de AWS Lambda incluidas para acceder a los servicios de AWS. De forma predeterminada, su alcance se reduce a los permisos mínimos requeridos. Para implementar una pila de AWS CloudFormation que crea o modifica roles de IAM, se debe proporcionar el valor `CAPABILITY_IAM` para `capabilities`. Si no se proporciona permiso a través de este mensaje, para implementar este ejemplo debe pasar explícitamente `--capabilities CAPABILITY_IAM` al comando `sam deploy`.

- **Disable rollback**: YES para hacer rollback si nuestro deploy causa errores, deshace todos los recursos creados durante el deploy fallido. NO para mantener los recursos creados durante el deploy aún cuando el deploy haya sido fallido.

- **Save arguments to configuration file**: YES para guardar todos los argumentos del deploy en el archivo de configuración (el archivo por default es `samconfig.toml`). NO para no guardar los argumentos del deploy en un archivo de configuración.

- **SAM configuration file [samconfig.toml]**: nombre del archivo donde se guardarán las configuraciones del deploy. Por default elige el archivo `samconfig.toml` si quieres guardarlo en ese archivo da ENTER. Si no, escribe el nombre del archivo donde quieres guardar la configuración.

- **SAM configuration environment [default]**: Ambiente de configuración donde tienes guardadas las Access Keys de tu cuenta AWS. Para visualizar esas Access Key revisa el archivo de configuración local de tus credenciales AWS. Si la configuracion es para otro ambiente entonces escribe el nombre del ambiente. Ejemplo: develop o test

```bash
    C:\Users\${username}\.aws\credentials
```

Si tu deploy se realizó correctamente aparecerá un mensaje como este en tu terminal.

```bash
Successfully created/updated stack ${Stack-name}...
```

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
ejemplo-tony-sam-app$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
ejemplo-tony-sam-app$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
ejemplo-tony-sam-app$ sam local start-api
ejemplo-tony-sam-app$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
Events:
  HelloWorld:
    Type: Api
    Properties:
      Path: /hello
      Method: get
```

## Add a resource to your application

The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
ejemplo-tony-sam-app$ sam logs -n HelloWorldFunction --stack-name "ejemplo-tony-sam-app" --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
ejemplo-tony-sam-app$ pip install -r tests/requirements.txt --user
# unit test
ejemplo-tony-sam-app$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
ejemplo-tony-sam-app$ AWS_SAM_STACK_NAME="ejemplo-tony-sam-app" python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "ejemplo-tony-sam-app"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
