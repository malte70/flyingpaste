# Database Layout

## Table `pastes`

+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name          | Type   | Description                                                                                                                                             |
+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| id            | string | The id used in the URL                                                                                                                                  |
| title         | string | The title, used if displayed as a web site                                                                                                              |
| description   | text   | Description of the paste, if a title is not enough                                                                                                      |
| author\_name  | string | The name/pseudonym of the uploader, default is "Anonymous"                                                                                              |
| author\_email | string | The EMail adress of the author, used for gravatar in web view                                                                                           |
| code          | text   | The actual pasted code/text (named code since text is a field type in many db systems, and because paste services mostly host source code/code snippets |
| language      | string | The language which will be used to provide syntax highlighting (which will be added soon)                                                               |
| privacy       | string | Privacy setting. Must be either `public`, `not\_listed` or `password:` followed by the password.                                                        |
+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+


