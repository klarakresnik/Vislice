% import model
%rebase('base.tpl', title='Vislice')

<table> 
  <tr>
      <td>
        <h2>{{igra.pravilni_del_gesla()}}</h2>
      </td>
  </tr>
  <tr>
      <td>
        <img src="../img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">
      </td>
  </tr>
  <tr>
      <td>
        Nepravilni ugibi: {{igra.nepravilni_ugibi()}}
      </td>
  </tr>
  <tr>
      <td>
        Preostali poskusi: {{igra.stevilo_napak()}} / {{model.STEVILO_DOVOLJENIH_NAPAK + 1}}
      </td>
  </tr>
</table>

% if poskus == model.ZMAGA:
<h1>ZMAGA!!!</h1>

<form action="/nova_igra/" method="post">
    <button type="submit">Nova igra (z računalnikom)</button>
</form>

<form action="/nova_igra/" method="post">
    <button type="submit">Nova igra (s prijateljem)</button>
</form>

% elif poskus == model.PORAZ:
<h1>BUHUUU LOSER</h1>

Pravilno gelso je bilo {{igra.geslo}}

<form action="/igra/" method="post">
    <button type="submit">Nova igra (z računalnikom)</button>
</form>

<form action="/igra/" method="post">
    <button type="submit">Nova igra (s prijateljem)</button>
</form>

% else:

<form action="/igra/" method="post">
    Črka: <input type='text' name='crka' autofocus>    
    <button type="submit">Pošlji ugib</button>
</form>

% end