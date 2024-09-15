<h1>Manual Testing Steps</h1>


| Item | Description                                               | Steps                                                                                         | Expected Result                                                                                           | Actual Result                                                                                           | Pass/Fail                                                                                                   |
|------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1    | Create account                                            | Go to register.html and populate all fields                                                    | New user object is created and new user is logged in automatically.                                      | New user object is created and new user is logged in automatically.                                      | Pass                                                                                                      |
| 2    | Create account with password with less than 8 characters | Go to register.html and populate all fields but with 7 char password.                         | Prompt informs user to add more characters to password.                                                    | Prompt informs user to add more characters to password.                                                    | Pass                                                                                                      |
| 3    | Create account with non-matching passwords               | Go to register.html and populate all fields but with non-matching passwords.                  | Prompt informs user that passwords don't match.                                                           | Prompt informs user that passwords don't match.                                                           | Pass                                                                                                      |
| 4    | Create account with an existing username                 | Go to register.html and populate all fields but with an already existing username.             | Prompt informs username already exists.                                                                  | Prompt informs username already exists.                                                                  | Pass (Initial Fail, as function was missing error validation)                                              |
| 5    | Create account with an existing email address             | Go to register.html and populate all fields but with an already existing email address.        | Prompt informs email already exists.                                                                      | Prompt informs email already exists.                                                                      | Pass (Initial Fail, as function was missing error validation)                                              |
| 6    | Create account with missing username field               | Go to register.html and populate all fields but username.                                      | Prompt informs username is missing.                                                                       | Prompt informs username is missing.                                                                       | Pass                                                                                                      |
| 7    | Create account with missing email field                  | Go to register.html and populate all fields but email.                                         | Prompt informs email is missing.                                                                          | Prompt informs email is missing.                                                                          | Pass                                                                                                      |
| 8    | Login with username that doesn't exist                   | Go to index.html and enter username that doesn't exist.                                        | Prompt informs username doesn't exist.                                                                    | Prompt informs username doesn't exist.                                                                    | Pass                                                                                                      |
| 9    | Login with username that exists but wrong password       | Go to index.html and enter username with wrong password.                                       | Prompt informs password is wrong.                                                                         | Prompt informs password is wrong.                                                                         | Pass                                                                                                      |
| 10   | Switch user type from Grantee to Granter                  | Go to admin.html and click on the right-hand side column to the username we want to change status of. | Page is refreshed, with currently changed status on the left column (Granter) and new status on the right if user wants to switch again. (Grantee) | Page is refreshed, with currently changed status on the left column (Granter) and new status on the right if user wants to switch again. (Grantee) | Pass                                                                                                      |
| 11   | Switch user type from Granter to Grantee                  | Go to admin.html and click on the right-hand side column to the username we want to change status of. | Page is refreshed, with currently changed status on the left column (Grantee) and new status on the right if user wants to switch again. (Granter) | Page is refreshed, with currently changed status on the left column (Grantee) and new status on the right if user wants to switch again. (Granter) | Pass                                                                                                      |
| 12   | Granter can create a new grant                            | From dashboard, Granter clicks on create a new grant and accesses the page of the same name. Granter populates all fields and clicks submit. | Upon successful completion, Granter is prompted confirmation the grant has been created and redirected to show-grant.html. | Upon successful completion, Granter is prompted confirmation the grant has been created and redirected to show-grant.html. | Pass                                                                                                      |
| 13   | Granter can only create a grant if all fields are completed | On create new grant page, click submit with one missing field.                                  | Granter prompted to fill missing field.                                                                   | Granter prompted to fill missing field.                                                                   | Pass                                                                                                      |
| 14   | Granter receives a message if grant value exceeds integer | On create new grant page, add value outside of range: -2,147,483,648 to 2,147,483,647.         | Granter prompted to enter a value within range.                                                          | Granter prompted to enter a value within range.                                                          | Pass                                                                                                      |
| 15   | Granter can see grant created after redirection to show_grant() | After creating grant and being redirected, look at redirected page to see grant information entered previously. | When redirected to show_grant(), Granter can see the grant created and populated fields.                  | When redirected to show_grant(), Granter can see the grant created and populated fields.                  | Pass                                                                                                      |
| 16   | Granter cannot activate grant without creating one question | On show_grant template, click submit application button.                                        | Submit button is not active and nothing happens.                                                          | Submit button is not active and nothing happens.                                                          | Pass                                                                                                      |
| 17   | Granter can delete grant                                  | Granter deletes grant on show_grant template.                                                   | Grant is deleted and Granter is redirected to dashboard.                                                   | Grant is deleted and Granter is redirected to dashboard.                                                   | Pass                                                                                                      |
| 18   | Granter cannot delete grant after making grant active    | Try to delete grant after making it active.                                                     | Delete button is not displayed.                                                                           | Delete button is not displayed.                                                                           | Pass                                                                                                      |
| 19   | After adding first question, Granter can activate the grant. | After submitting the first question, upon refresh activate button becomes green and user can click. | Upon clicking on button, grant is displayed as active on screen and on database.                          | Upon clicking on button, grant is displayed as active on screen and on database.                          | Pass                                                                                                      |
| 20   | Granter can add more questions                            | Granter adds more questions in the add question section and presses submit.                     | Upon pressing submit, question is added to database and displayed on template.                            | Upon pressing submit, question is added to database and displayed on template.                            | Pass                                                                                                      |
| 21   | Granter can edit question                                 | Granter can edit question by clicking on the edit button and submit newly edited text.           | By clicking on the edit button, Granter is redirected to the edit question template. Upon entering new question value and submitting, user is redirected to show-grant template. | By clicking on the edit button, Granter is redirected to the edit question template. Upon entering new question value and submitting, user is redirected to show-grant template. | Pass                                                                                                      |
| 22   | Granter can delete question only if grant is not activated | Granter can delete question by clicking on delete button, only when associated grant is not active. | Deleted question is removed from database, but action not possible if grant is active. If grant is active, delete button is not accessible to Granter on template. | Deleted question is removed from database, but action not possible if grant is active. If grant is active, delete button is not accessible to Granter on template. | Pass                                                                                                      |
| 23   | Grantee can access grants available from dashboard and see the status of their applications | Go on Grantee dashboard template.                                                                 | Grantee can scroll up and down on dashboard to see 2 sections (1) grants available and (2) see the status of their current application. | Grantee can scroll up and down on dashboard to see 2 sections (1) grants available and (2) see the status of their current application. | Pass                                                                                                      |
| 24   | Grantee can apply to an active grant                      | From dashboard, Grantee clicks on Apply and is redirected to grants available template. Grantee clicks on any grant available through apply button. | By clicking on apply button, an application object is created in the backend and redirects Grantee to apply-to-grant.html with application ID as a parameter and can start answering questions and click submit to save them on the database. | By clicking on apply button, an application object is created in the backend and redirects Grantee to apply-to-grant.html with application ID as a parameter and can start answering questions and click submit to save them on the database. | Pass                                                                                                      |
| 25   | Grantee can leave application and come back to it later  | Grantee submits an answer but does not submit the application. Leaves the page and comes back.   | After leaving the application page, user can access the application where they left it as the grants-available template will redirect the user to their application object that relates to the grant they applied to. | After leaving the application page, user can access the application where they left it as the grants-available template will redirect the user to their application object that relates to the grant they applied to. | Pass                                                                                                      |
| 26   | Grantee cannot submit an application unless they answered all questions available at the moment of the application | Try to submit an application where not all questions have been answered.                        | Nothing happens.                                                                                           | Nothing happens.                                                                                           | Pass                                                                                                      |
| 27   | Grantee can edit their answers                            | Grantee clicks on edit from apply-to-grant to change answer value.                              | Upon editing, the new answer is saved on the database and displayed on the template.                      | Upon editing, the new answer is saved on the database and displayed on the template.                      | Pass                                                                                                      |
| 28   | Grantee can delete their answers                          | Grantee clicks on delete from apply-to-grant to delete object.                                  | Upon deleting, the answer object is deleted from the database and not shown on the template.              | Upon deleting, the answer object is deleted from the database and not shown on the template.              | Pass                                                                                                      |
| 29   | Grantee can delete their application                      | Grantee clicks on delete application from apply-to-grant to delete object. This can also be achieved after submission through read-submitted-application template. | Upon deleting, the application object is deleted from the database and not shown on the template.         | Upon deleting, the application object is deleted from the database and not shown on the template.         | Pass                                                                                                      |
| 30   | When deleting their application, the associated GrantAnswer objects are also deleted | Create application, answer a question. Delete application.                                       | Answers linked to deleted application are deleted from the database.                                        | Answers linked to deleted application are deleted from the database.                                        | Pass after adding Cascade to GrantApplication model.                                                        |
| 31   | After submitting their application, Grantee cannot edit their application. | Submit application as Grantee. Access application from dashboard or grants available.            | Edit button not available.                                                                               | Edit button not available.                                                                               | Pass                                                                                                      |
| 32   | After submitting their application, Grantee can delete their application. | Submit application as Grantee. Access application from dashboard or grants available.            | Grantee can delete application. Application is deleted from the database.                                 | Grantee can delete application. Application is deleted from the database.                                 | Pass                                                                                                      |
| 33   | After submitting their application, Grantee can see the status of their application | Submit application. Go to dashboard or grants available template.                                | Submitted application status is visible.                                                                  | Application status is visible.                                                                            | Pass                                                                                                      |
| 34   | After activating the grant, Granters can edit the grant with new questions or edit existing questions. | As Granter, activate grant and go back to show grant template to edit or add questions.          | Granter can edit or add questions after activating grant.                                                 | Granter can edit or add questions after activating grant.                                                 | Pass                                                                                                      |
| 35   | After activating the grant, or closing it, Granter cannot delete the grant | As Granter, activate grant and go back to show grant template to delete it.                      | Delete button is not available.                                                                           | Delete button is not available.                                                                           | Pass                                                                                                      |
| 36   | Granter can access submitted applications from Grantee   | From Granter dashboard, click “applications” and select an application by clicking “open”.        | Granter is redirected to Grantee application.                                                             | Granter is redirected to Grantee application.                                                             | Pass                                                                                                      |
| 37   | Granter can reject Grantee application                    | From show-user-grant-application.html, Granter scrolls down and clicks on reject application.    | Application is marked as rejected in database and displayed in show-all-grant-application template.       | Application is marked as rejected in database and displayed in show-all-grant-application template.       | Pass                                                                                                      |
| 38   | Granter can approve Grantee application                   | From show-user-grant-application.html, Granter scrolls down and clicks on approve application.   | Application is marked as approved in database and approved is displayed in show-all-grant-application template. | Application is marked as approved in database and approved is displayed in show-all-grant-application template. | Pass                                                                                                      |
| 39   | Grantee can see from their dashboard if their application has been approved or rejected. | Connect to dashboard as Grantee and see newly updated status.                                    | Application status is updated.                                                                            | Application status is updated.                                                                            | Pass                                                                                                      |
| 40   | Users (Grantee & Granter) can see their account details    | Go to navbar and click on “account details”.                                                      | User is redirected to account page and can see account details.                                           | User is redirected to account page and can see account details.                                           | Pass                                                                                                      |
| 41   | Users (Grantee & Granter) can delete their account        | Go to navbar and click on “account details”. Click “delete”.                                      | User account is deleted.                                                                                   | User account is deleted.                                                                                   | Pass                                                                                                      |
| 42   | Grantee’s applications are still available in the database after Grantee deletes their account. | Interrogate database from command line (to find command line, go to the bottom of this table).    | Application is still available in database under user None but not displayed on front end.               | Application is still available in database under user None but not displayed on front end.               | Pass                                                                                                      |
| 43   | Navbar - User is redirected to their respective dashboard when clicking on their username (orange) on top left. | Click username on top left of navbar.                                                             | Users are redirected to Grantee dashboard (if Grantee) or Granter dashboard (if Granter).                 | Users are redirected to Grantee dashboard (if Grantee) or Granter dashboard (if Granter).                 | Pass                                                                                                      |
| 44   | Navbar - Grantee is redirected to Grantee dashboard when clicking on “dashboard” | Click “dashboard” on navbar as Grantee.                                                          | Grantee redirected to dashboard.                                                                          | Grantee redirected to dashboard.                                                                          | Pass                                                                                                      |
| 45   | Navbar - Grantee is redirected to Grants Available when clicking on “Grants” | Click “Grants” on navbar as Grantee.                                                              | Grantee redirected to Grants Available template.                                                          | Grantee redirected to Grants Available template.                                                          | Pass                                                                                                      |
| 46   | Navbar - Grantee can log out                              | Go to navbar, click “logout”.                                                                     | Grantee is logged out.                                                                                     | Grantee is logged out.                                                                                     | Pass                                                                                                      |
| 47   | Navbar - Granter is redirected to Granter dashboard when clicking on “dashboard” | Click “dashboard” on navbar as Granter.                                                           | Redirected to Granter dashboard.                                                                          | Redirected to Granter dashboard.                                                                          | Pass                                                                                                      |
| 48   | Navbar - Granter is redirected to create-new-grant.html when clicking on “Create new grant” | Click “Create New Grant” on navbar as Granter.                                                    | Redirected to create-new-grant.html.                                                                      | Redirected to create-new-grant.html.                                                                      | Pass                                                                                                      |
| 49   | 500 error - user receives 500 template when causing internal server error | Access link: (grant-management-mp3-709b64ecedb2.herokuapp.com)                                     | Customer 500 error template shows.                                                                        | Customer 500 error template shows.                                                                        | Pass                                                                                                      |
| 50   | 404 error - user receives 404 template when causing internal server error | Create 404 error by accessing a page that doesn’t exist domain/new_page                            | Customer 404 error template shows.                                                                        | Customer 404 error template shows.                                                                        | Pass                                                                                                      |
| 51   | Access restriction - Grantee cannot access Granter Dashboard() | Try to access Granter dashboard as Grantee through URL.                                          | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 52   | Access restriction - Grantee cannot access create_new_grant() | Try to access create_new_grant() as Grantee through URL.                                         | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 53   | Access restriction - Grantee cannot access show_grant()   | Try to access show_grant() as Grantee through URL.                                               | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 54   | Access restriction - Grantee cannot access delete_grant() | Try to access delete_grant() as Grantee through URL.                                              | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 55   | Access restriction - Grantee cannot access activate_grant() | Try to access activate_grant() as Grantee through URL.                                            | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 56   | Access restriction - Grantee cannot access deactivate_grant() | Try to access deactivate_grant() as Grantee through URL.                                          | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 57   | Access restriction - Grantee cannot access close_grant() | Try to access close_grant() as Grantee through URL.                                               | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 58   | Access restriction - Grantee cannot access create_new_grant_question() | Try to access create_new_grant_question() as Grantee through URL.                                | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 59   | Access restriction - Grantee cannot access edit_show_grant_question() | Try to access edit_show_grant_question() as Grantee through URL.                                  | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 60   | Access restriction - Grantee cannot access delete_show_grant_question() | Try to access delete_show_grant_question() as Grantee through URL.                                | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 61   | Access restriction - Grantee cannot access show_all_grant_application() | Try to access show_all_grant_application() as Grantee through URL.                                | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 62   | Access restriction - Grantee cannot access show_user_grant_application_id() | Try to access show_user_grant_application_id() as Grantee through URL.                           | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 63   | Access restriction - Grantee cannot access reject_user_grant_application_id() | Try to access reject_user_grant_application_id() as Grantee through URL.                         | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 64   | Access restriction - Grantee cannot access approve_user_grant_application_id() | Try to access approve_user_grant_application_id() as Grantee through URL.                        | Redirected to Grantee dashboard.                                                                          | Redirected to Grantee dashboard.                                                                          | Pass                                                                                                      |
| 65   | Heroku version is set on production                        | Under line: app.config['DEBUG'] = False                                                            | Console shows: Running in production mode                                                                  | Console shows: Running in production mode                                                                  | Pass                                                                                                      |
| 66   | Footer - YouTube icon redirects to YouTube                 | Click on icon.                                                                                   | User is redirected to YouTube.                                                                            | User is redirected to YouTube.                                                                            | Pass                                                                                                      |
| 67   | Footer - X icon redirects to X                             | Click on icon.                                                                                   | User is redirected to X.                                                                                  | User is redirected to X.                                                                                  | Pass                                                                                                      |
| 68   | Footer - Instagram icon redirects to Instagram             | Click on icon.                                                                                   | User is redirected to Instagram.                                                                          | User is redirected to Instagram.                                                                          | Pass                                                                                                      |
| 69   | Footer - Facebook icon redirects to Facebook               | Click on icon.                                                                                   | User is redirected to Facebook.                                                                            | User is redirected to Facebook.                                                                            | Pass                                                                                                      |



**Database query for #42**:

run `flask shell`

In the shell write the following lines:
    from app import db, GrantApplication
    applications = GrantApplication.query.all()
    for application in applications:
        print(f"Application ID: {application.id}, User ID: {application.user_id}")

To leave shell, type: `exit()`