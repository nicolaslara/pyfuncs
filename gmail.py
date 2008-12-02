import poplib, smtplib

pop = poplib.POP3_SSL('pop.gmail.com')
pop.user('carlostaibo@gmail.com')
pop.pass_('hola_mi_lindisimo_coliflor')

message_count, mailbox_size = pop.stat()


mess = pop.retr(1)

pop.quit()


mess[1][8]     # Este es el from
mess[1][10]    # Este es el subject
mess[1][20]    # Este es el cuerpo de las suecas


to_list = ['carlostaibo@gmail.com']
from_list = ['nicolaslara@gmail.com']
mensaje = mess[1][20] + " <b> hola</b>"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()
server.login('carlostaibo@gmail.com', 'cositarica')

server.sendmail(from_list, to_list, mensaje)

server.close()
