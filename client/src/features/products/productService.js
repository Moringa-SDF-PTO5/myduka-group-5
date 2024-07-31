const PRODUCTS_API = 'https://myduka-api.onrender.com/api/products'

//Get all products
async function getAllProducts() {
    const response = await fetch(PRODUCTS_API)

    const responseData = await response.json()

    return responseData.data
}

//Get one product
async function getOneProduct(productItemId) {
    const response = await fetch(`${PRODUCTS_API}/${productItemId}`)

    const responseData = await response.json()

    if (responseData.data === null) {
        throw new Error(responseData.message)
    }

    return responseData.data
}

//Edit one product
async function editOneProduct(productItemId, updateData) {
    const response = await fetch(`${PRODUCTS_API}/${productItemId}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updateData),
    })

    const responseData = await response.json()

    if (responseData.data === null) {
        throw new Error(responseData.message)
    }

    return responseData.data
}

//Add a product
async function addProduct(productData) {
    const response = await fetch(PRODUCTS_API, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(productData),
    })

    const responseData = await response.json()

    if (responseData.data === null) {
        throw new Error(responseData.message)
    }

    return responseData.data
}

const productService = {
    getAllProducts,
    getOneProduct,
    editOneProduct,
    addProduct,
}

export default productService
