var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('ProductId: ',productId,'action: ',action);
        console.log('User',user);
        if(user === 'AnonymousUser'){
            console.log('not logged in');
        }else{
            console.log('User is logged in, sending data....');
        }
    });
}